from sqlalchemy.orm import Session
from usm_day_pass.core.repositories.tables import HotelModel
from usm_day_pass.core.entities import Hotel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import typing as t
from sqlalchemy.exc import SQLAlchemyError


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PassesRepository:
    def __init__(self, db: Session, logger: logging.Logger = None):
        self.db = db
        self.logger = logger

    def add(self, club: Hotel):
        club = HotelModel.from_entity(club)
        self.db.add(club)
        self.db.commit()
        self.db.refresh(club)
        return club.to_entity()

    def get_by_id(self, id: int):
        club = self.db.query(HotelModel).filter(HotelModel.id == id).first()
        return club.to_entity() if club else None

    def get_all(self) -> t.Union[t.List[Hotel] | None]:
        self.logger.info("Fetching all places in database...")
        try:
            clubs = self.db.query(HotelModel).all()
        except SQLAlchemyError as e:
            self.logger.error("Error while fetching places: %s" % (str(e)))
            return None
        return [club.to_entity() for club in clubs]

    def delete(self, id: int):
        club = self.db.query(HotelModel).filter(HotelModel.id == id).first()
        if club:
            self.db.delete(club)
            self.db.commit()
