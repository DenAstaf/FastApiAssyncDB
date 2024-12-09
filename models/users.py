from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'  # Имя таблицы в базе данных

    id: Mapped[int] = mapped_column(primary_key=True)  # Столбец id
    name: Mapped[str] = mapped_column(nullable=False)  # Столбец name
    username: Mapped[str] = mapped_column(unique=True)  # Столбец name
    email: Mapped[str | None] = mapped_column(unique=True)  # Столбец age

    # Устанавливает отношение один к одному с таблицей posts
    posts = relationship("Post", back_populates="user")
