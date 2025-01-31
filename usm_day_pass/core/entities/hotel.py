from dataclasses import dataclass
from typing import Optional


@dataclass
class Hotel:
    id: int
    name: str
    stars: int
    price: float
    restaurant: bool
    childs_allowed: Optional[bool] 

    def validate(self):
        if self.price <= 0:
            raise ValueError("The price should not be greater than 0.")
        if not self.name:
            raise ValueError("The name should not be empty.")
        
    def to(self):
        """Converts current 'Hotel' instance in dict"""
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }
