from __future__ import annotations
import sqlite3


class SingletonMeta(type):
    """Meta type of Singleton Class"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.instance = sqlite3.connect(":memory:")
        self.cursor = self.instance.cursor()
        self.cursor.execute(
            "CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)"
        )

    @property
    def connection(self):
        return self.cursor


"""
In this approach, when the class is instantiated for first time,
the initializer method is called and all the necessary parameters
are initialized. Later on, whenever the application reinstantiate
the class, the same object is returned to the context.
"""


if __name__ == "__main__":
    db = Database()
    db.connection.execute("INSERT INTO user(name) VALUES ('Ram')")
    # Instantiated from some another function
    db_again = Database()
    resp = db_again.connection.execute("SELECT id, name FROM user").fetchall()
    print(resp)
