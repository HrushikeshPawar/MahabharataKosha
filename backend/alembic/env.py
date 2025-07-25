import os
import sys
from pathlib import Path
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from dotenv import load_dotenv

from alembic import context

# Add the parent directory (the project's root) to the Python path.
# This ensures that Alembic can find your 'app' module and its models.
sys.path.append(str(Path(__file__).resolve().parents[1]))

# --- Import your models' Base object ---
# This is the declarative base from which all your models inherit.
# Alembic uses this to detect the schema changes.
from app.models import Base # type: ignore

# Load environment variables from a .env file.
# This is crucial for loading the DATABASE_URL when running migrations.
load_dotenv()

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Set the target metadata for autogeneration ---
# This tells Alembic that your models' metadata is the target schema.
target_metadata = Base.metadata

# Set the database URL from the environment variable.
# This overrides the value in alembic.ini, ensuring the correct URL is used.
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("DATABASE_URL environment variable is not set.")
config.set_main_option("sqlalchemy.url", db_url)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
