from typing import TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .adhyaya import Adhyaya  # Avoid circular import


class Parva(Base):
    __tablename__ = "parvas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title_sanskrit: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True
    )
    title_english: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    parva_num: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    adhyayas: Mapped[list["Adhyaya"]] = relationship("Adhyaya", back_populates="parva")

    def __repr__(self) -> str:
        return f"<Parva(id={self.id}, title_english='{self.title_english}')>"
