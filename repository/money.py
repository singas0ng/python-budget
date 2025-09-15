from models.money import Money
from .base import BaseRepository as Base
from sqlmodel import Session, select
from typing import Optional, List

class MoneyRepository(Base):
    def __init__(self, db: Session):
        super().__init__(Money, db)

    def getList(self, page: int = 0, count: int = 10) -> List[Money]:
        return self.db.exec(select(Money).offset(page * count).limit(count)).all()

    def create(self, money: Money) -> Money:
        self.db.add(money)
        self.db.commit()
        self.db.refresh(money)

        return money

    def update(self, id: int, money: Money) -> Money:
        origin = self.db.get(Money, id)
        self.update_object(origin, money)

        self.db.commit()
        self.db.refresh(origin)

        return origin