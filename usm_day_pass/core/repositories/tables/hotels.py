from dataclasses import dataclass
from typing import Optional, Type
from usm_day_pass.core.entities import Hotel
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
)
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class HotelModel(Base):
    __tablename__ = "clubs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    stars = Column(Integer, nullable=False)
    price = Column(Float, nullable=False) 
    restaurant = Column(Boolean, nullable=False)
    childs_allowed = Column(Boolean, nullable=True)
    photo_url = Column(String, nullable=True)
    
    def to_entity(self):
        return Hotel(
            id=self.id,
            name=self.name,
            stars=self.stars,
            price=self.price,
            restaurant=self.restaurant,
            childs_allowed=self.childs_allowed,
            photo_url=self.photo_url
        ) 
    
    @staticmethod 
    def from_entity(hotel: Hotel, cls: "HotelModel") -> "HotelModel":
        """
        Converts core entity into an SQLAlchemy model

        :param hotel:
            Hotel to convert as model
        :param cls:
            HotelModel constructor to call on 'hotel'
        """
        
        return cls(
            id=hotel.id,
            name=hotel.name,
            stars=hotel.stars,
            price=hotel.price,
            restaurant=hotel.restaurant,
            childs_allowed=hotel.childs_allowed,
            photo_url=hotel.photo_url
        ) 