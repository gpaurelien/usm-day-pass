import typing as t

class Pass(t.Protocol):
    def list(self):
        """List all hotels providing day passes""" 

    def get_pass_stars(self, stars: int) -> t.List[Hotel]:  # TODO: create Hotel model in core
        """Collect passes from 5-star hotels"""