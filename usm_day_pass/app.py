import typing as t
import logging
from usm_day_pass.core import repositories as r
from usm_day_pass.core import interfaces
from usm_day_pass.core import services as s
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from usm_day_pass.config import config


db_name, engine = config.DATABASE_NAME, create_engine(config.DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Core:
    def __init__(
        self,
        logger: t.Optional[logging.Logger] = None,
    ):
        self.passes_repository: interfaces.PassesRepository = r.PassesRepository(
            db,
            logger=logger
        )
        self.passes_service = s.Passes(self.passes_repository, logger)