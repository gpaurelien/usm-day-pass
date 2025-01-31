import typing as t
import logging
from usm_day_pass import repositories
from usm_day_pass.core import interfaces
from usm_day_pass.core import services
import os


db = os.getenv("DATABASE_NAME")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Core:
    def __init__(
        self,
        logger: t.Optional[logging.Logger] = None,
    ):
        self.passes_adapter: interfaces.Passes = repositories.Passes(db)
        self.passes_service = services.Passes(self.passes_adapter, logger)