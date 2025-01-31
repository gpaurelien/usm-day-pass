from dataclasses import dataclass
from typing import Optional
from usm_day_pass.core.entities import Hotel


@dataclass(frozen=True)
class HotelModel:
    id: int
    name: str
    stars: int
    price: float
    restaurant: bool
    childs_allowed: Optional[bool] 

    def to_entity(self):
        return Hotel(
            self.name,
            self.stars,
            self.price,
            self.restaurant,
            self.childs_allowed
        )