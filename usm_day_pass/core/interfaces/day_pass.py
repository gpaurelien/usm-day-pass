import typing as t
from usm_day_pass.core.entities import Hotel


class Passes(t.Protocol):
    def list(self) -> t.List[Hotel]:
        """List all hotels providing day passes""" 

    def get_pass_stars(self, stars: int) -> t.List[Hotel]:
        """Collect passes from 5-star hotels"""