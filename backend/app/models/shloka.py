from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey, Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base

if TYPE_CHECKING:
    from .adhyaya import Adhyaya  # Avoid circular import
    from .feedback import Feedback  # Avoid circular import


class Shloka(Base):
    __tablename__ = "shlokas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # The BORI Unique Identifier (parsed from the source file)
    parva_num: Mapped[int] = mapped_column(Integer, nullable=False)
    adhyaya_num: Mapped[int] = mapped_column(Integer, nullable=False)
    shloka_num: Mapped[int] = mapped_column(Integer, nullable=False)  # Verse number
    pada_char: Mapped[str] = mapped_column(Text, nullable=False)

    # The actual text content
    text_sanskrit: Mapped[str] = mapped_column(
        Text, nullable=False
    )  # Original Sanskrit
    text_sanskrit_split: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True
    )  # Sanskrit with compounds split
    text_english: Mapped[str] = mapped_column(
        Text, nullable=False
    )  # English translation

    #  Rich metadata for future NLP use cases, storing pre-computed linguistic analysis
    line_type: Mapped[str] = mapped_column(
        Enum("VERSE", "PROSE", "HEADER", name="line_type_enum", create_type=False),
        default="VERSE",
        nullable=False,
    )
    linguistic_analysis: Mapped[Optional[dict]] = mapped_column(
        JSONB, nullable=True
    )  # For NLP results

    # Relationships (Less critical for lookup now, but still good for structure)
    adhyaya_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("adhyayas.id"), nullable=False
    )
    adhyaya: Mapped["Adhyaya"] = relationship("Adhyaya", back_populates="shlokas")

    # Setting up for multilingual explanations later on.
    explanation_english: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    explanation_marathi: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)

    feedbacks: Mapped[list["Feedback"]] = relationship(
        "Feedback", back_populates="shloka"
    )

    def __repr__(self) -> str:
        return f"<Shloka(id={self.id}, parva={self.parva_num}, adhyaya={self.adhyaya_num}, shloka={self.shloka_num})>"
