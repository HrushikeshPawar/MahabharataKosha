from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .adhyaya import Adhyaya  # Avoid circular import


class Shloka(Base):
    __tablename__ = "shlokas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    shloka_num: Mapped[int] = mapped_column(Integer, nullable=False)
    text_sanskrit: Mapped[str] = mapped_column(Text, nullable=False)
    text_english: Mapped[str] = mapped_column(Text, nullable=False)
    adhyaya_id: Mapped[int] = mapped_column(Integer, ForeignKey("adhyayas.id"), nullable=False)

    adhyaya: Mapped["Adhyaya"] = relationship("Adhyaya", back_populates="shlokas")

    def __repr__(self) -> str:
        return f"<Shloka(id={self.id}, shloka_num='{self.shloka_num}')>"