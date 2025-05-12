from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "login": self.login,
            # do not serialize the password, its a security breach
        }
    
class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
   
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
  
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    eye_color: Mapped[str] = mapped_column(String(120), nullable=False)
    Hair_color: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color
        }

class Planets(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=False)
    terrain: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
        }