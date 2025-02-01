import typing as t
from usm_day_pass.core.entities import Hotel


class PassesRepository(t.Protocol):
    def add(self, club: Hotel) -> Hotel:
        """Add an entry in database"""

    def get_by_id(self, id: int) -> t.Union[Hotel | None]:
        """Retrieve a resort by its id"""

    def get_all(self) -> t.List[Hotel]:
        """Retrieve all places in database"""

    def delete(self, id: int) -> None:
        """Delete an entry according to an id"""