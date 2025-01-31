from usm_day_pass.core import interfaces
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Passes:
    def __init__(
        self,
        passes_adapter: interfaces.Passes,
        logger: logging.Logger = logger,
    ) -> None:
        self.passes_adapter = passes_adapter
        self.logger = logger

    def list(self) -> list:
        return self.passes_adapter.list()

    def get_pass_stars(self, stars: int) -> list:
        return self.passes_adapter.get_pass_stars(stars) 