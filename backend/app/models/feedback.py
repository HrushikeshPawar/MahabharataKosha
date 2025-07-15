from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .shloka import Shloka  # Avoid circular import

class Feedback(Base):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shloka_id: Mapped[int] = mapped_column(Integer, ForeignKey("shlokas.id"), nullable=False)
    language: Mapped[str] = mapped_column(String(10), nullable=False) # 'english' or 'marathi'
    rating: Mapped[int] = mapped_column(Integer, nullable=False) # e.g., 1 for "unhelpful", 5 for "very helpful"
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    # user_id or session_id can be added later

    shloka: Mapped["Shloka"] = relationship("Shloka", back_populates="feedbacks")
