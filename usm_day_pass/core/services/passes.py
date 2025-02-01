from usm_day_pass.core import interfaces
import logging
import typing as t
from usm_day_pass.core.entities import Hotel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Passes:
    def __init__(
        self,
        passes_repository: interfaces.PassesRepository,
        logger: logging.Logger = logger,
    ) -> None:
        self.passes_repository = passes_repository
        self.logger = logger

    def list(self, to_dict: bool = False) -> t.List[Hotel]:
        clubs = self.passes_repository.get_all()
        if to_dict:
            for club in clubs:
                club.to()
            return clubs
        return clubs  # will be jsonified

    def get_pass_stars(self, stars: int) -> list:
        pass
