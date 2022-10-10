from dataclasses import dataclass, field
from typing import Any, Dict, List, Protocol
import typing
import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:")
metadata = sa.MetaData()

# ===========
#  SQL Table
# ===========
users = sa.Table(  # Service
    "core_users",
    metadata,
    sa.Column("id", sa.Integer(), primary_key=True),
    sa.Column("name", sa.String(length=32), nullable=False),
)


metadata.create_all(bind=engine)


# ===========
# Domain Model
# ===========


@dataclass(init=False)
class DomainModel:
    id: int


@dataclass
class User(DomainModel):
    name: str


def user_factory(id: int = None, name: str = "") -> User:
    return User(id=id, name=name)


# ============
# Protocols/Interfaces
# ============


class Connection(Protocol):
    def commit(self):
        ...

    def rollback(self):
        ...

    def execute(self):
        ...

    def execute_many(self):
        ...

    def fetch_all(self):
        ...

    def fetch_one(self):
        ...


class Repository(Protocol):  # Client Interface
    def get(self, id: int) -> DomainModel:
        ...

    def list(self) -> List[DomainModel]:
        ...

    def create(self, model: DomainModel) -> int:
        ...

    def update(self, model: DomainModel) -> None:
        ...


# ==========
# Adapter
# ==========


class UserSqlRepository:  # Adapter
    def __init__(self, db: Connection):
        self.db = db

    def get(self, id: int) -> User:
        data = self.db.fetch_one(users.select().where(id=id))
        return User(id=data[0], name=data[1])

    def list(self) -> List[User]:
        data = [
            User(id=d[0], name=d[1]) for d in self.db.execute(users.select()).fetchall()
        ]
        return data

    def create(self, model: User) -> User:
        cursor_result = self.db.execute(
            users.insert({users.c.name.key: model.name}),
        )
        model.id = cursor_result.lastrowid
        return model

    def update(self, model: User) -> None:
        self.db.execute(
            users.update({"name": model.name}).where(id=model.id),
        )


def client(db: Connection, repository: typing.Type[Repository]):  # client
    repo = repository(db=db)
    model = user_factory(name="Ram")
    model = repo.create(model)
    repo.create(user_factory(name="Sita"))
    print(repo.list())


"""
In this structural pattern, the client depends on an interface
for a third party service. In this given example of SqlAlchemy,
the users is a third party service in which the client is dependent on.
But It will quickly be mess if client calls straight to the
third party service functions. So client actually depend on the
abstraction over an adapter, which infact connect the client to
the actual functions in the service. Thus, the service are now
swappable for client by implementing another adapter.
"""


if __name__ == "__main__":
    print("Inside actual sqlite database")
    client(engine.connect(), repository=UserSqlRepository)

    class FakeRepository:
        def __init__(self, db: Connection):
            self.db = db

        def get(self, id: int) -> DomainModel:
            data = self.db.storage.get(id)
            return User(id=data["id"], name=data["name"])

        def list(self) -> List[DomainModel]:
            return [
                User(id=data["id"], name=data["name"])
                for data in self.db.storage.values()
            ]

        def create(self, model: DomainModel) -> int:
            id = self.db.id_counter
            self.db.storage[id] = {
                "id": id,
                "name": model.name,
            }
            self.db.id_counter += 1
            return id

        def update(self, model: DomainModel) -> None:
            self.db.storage[model.id].update(
                {
                    "name": model.name,
                }
            )

    @dataclass
    class FakeConnection:
        storage: Dict[int, Any] = field(default_factory=dict)
        id_counter: int = 1

    print("Inside in memory python dictionary")
    client(FakeConnection(), repository=FakeRepository)
