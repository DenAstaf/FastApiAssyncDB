from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Post(Base):
    __tablename__ = 'posts'  # Имя таблицы в базе данных

    id: Mapped[int] = mapped_column(primary_key=True)  # Столбец id
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))  # Столбец user_id
    title: Mapped[str | None] = mapped_column(nullable=True)  # Столбец title
    body: Mapped[str | None] = mapped_column(nullable=True)  # Столбец body

    # Устанавливает обратное отношение к таблице users
    user = relationship("User", back_populates="posts")
