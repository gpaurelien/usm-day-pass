import sqlite3
import typing as t
from usm_day_pass.core.entities import Hotel


class Passes:
    def __init__(self, db: str):
        self.db = sqlite3.connect(db, check_same_thread=False)

    def list(self) -> t.List[Hotel]:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clubs")
        rows = cursor.fetchall()        
        hotels = [Hotel(*row) for row in rows]
        return hotels

    def get_pass_stars(self, stars: int) -> t.List[Hotel]:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clubs WHERE stars = ?", (stars,))
        rows = cursor.fetchall()
        hotels = [Hotel(*row) for row in rows]
        return hotels

    def __del__(self):
        self.db.close()