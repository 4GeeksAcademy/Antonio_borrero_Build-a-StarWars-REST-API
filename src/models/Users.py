from sqlalchemy import String, Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import db
from typing import List

class Users(db.Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    users_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planets.id"))
    people_id: Mapped[int] = mapped_column(Integer, ForeignKey("people.id"))

    users: Mapped["Users"] = relationship("Users", back_populates="favorites")
    people: Mapped["People"] = relationship("People")
    planets: Mapped["Planets"] = relationship("Planets")