from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Hotel:
    id: int
    name: str
    stars: int
    price: float
    restaurant: bool
    childs_allowed: Optional[bool]
    photo_url: Optional[str] = None

    def validate(self):
        if self.price <= 0:
            raise ValueError("The price should be greater than 0.")
        if not self.name:
            raise ValueError("The name should not be empty.")
        
    def to(self):
        """Converts current 'Hotel' instance in dict"""
        return {key: value for key, value in self.__dict__.items()}
