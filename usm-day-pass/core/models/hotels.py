from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HotelModel:
    name: str
    stars: int
    price: float
    restaurant: bool
    childs_allowed: Optional[bool] 

    def to_entity(self):
        """Converts the model into an entity"""
        return 