import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, table_name: str, db_name: str) -> None:
        self.table_name = table_name
        self.db_name = db_name
        self._connection = sqlite3.connect(self.db_name)

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            f"VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        users = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        if not users:
            return []

        return [Actor(*user) for user in users]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            f"SET (first_name, last_name ) = (?, ?) "
            f"WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ? ",
            (pk,)
        )
        self._connection.commit()