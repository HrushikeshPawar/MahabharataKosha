from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .shloka import Shloka  # Avoid circular import
    from .parva import Parva  # Avoid circular import


class Adhyaya(Base):
    __tablename__ = "adhyayas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title_sanskrit: Mapped[str] = mapped_column(String, nullable=False)
    title_english: Mapped[str] = mapped_column(String, nullable=False)
    adhyaya_num: Mapped[int] = mapped_column(Integer, nullable=False)
    parva_id: Mapped[int] = mapped_column(Integer, ForeignKey("parvas.id"))

    parva: Mapped["Parva"] = relationship("Parva", back_populates="adhyayas")
    shlokas: Mapped[list["Shloka"]] = relationship("Shloka", back_populates="adhyaya")

    def __repr__(self) -> str:
        return f"<Adhyaya(id={self.id}, title_english='{self.title_english}')>"
