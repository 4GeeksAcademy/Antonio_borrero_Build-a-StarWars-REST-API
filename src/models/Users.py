from sqlalchemy import String, Boolean, Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import db
from typing import List
from models.People import People
from models.Planets import Planets

class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="users")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
    
class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    users: Mapped["Users"] = relationship(back_populates="favorites")

    people: Mapped[List["People"]] = relationship(secondary="people_favorites", back_populates="favorites")
    planets: Mapped[List["Planets"]] = relationship(secondary="planets_favorites", back_populates="favorites")

people_favorites = Table(
    "people_favorites",
    db.metadata,
    Column("people_id", ForeignKey("people.id")),
    Column("favorites_id", ForeignKey("favorites.id"))
)

planets_favorites = Table(
    "planets_favorites",
    db.metadata,
    Column("planets_id", ForeignKey("planets.id")),
    Column("favorites_id", ForeignKey("favorites.id"))
)