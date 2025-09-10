from .base import Controller

from fastapi import Depends
from typing import List, Optional
from datetime import datetime, date

from sqlmodel import Session, select

from models.money import Money as MoneyModel
from models.category import Category as CategoryModel

from database import get_db

class MoneyController(Controller):
    def __init__(self):
        super().__init__("/money")
        self._setup_routes()

    def _setup_routes(self):
        self.router.get("", response_model=List[MoneyModel])(self.get_money_list)
        self.router.get("/{id}", response_model=Optional[MoneyModel])(self.get_money)
        self.router.post("", response_model=MoneyModel)(self.create_money)
        self.router.put("/{id}", response_model=Optional[MoneyModel])(self.update_money)
        self.router.delete("/{id}", response_model=bool)(self.delete_money)

    # GET
    def get_money_list(self, db: Session = Depends(get_db)) -> List[MoneyModel]:
        results = db.exec(select(MoneyModel)).all()
        return results

    def get_money(self, id: int, db: Session = Depends(get_db)) -> Optional[MoneyModel]:

        # address_table, user_table.c.id == address_table.c.user_id
        statements = select(MoneyModel).where(
            MoneyModel.id == id
            ).join(
                CategoryModel,
                MoneyModel.id == CategoryModel.id
                )

        money = db.exec(statements).first()

        return money

    # POST
    def create_money(self, money: MoneyModel, db: Session = Depends(get_db)) -> MoneyModel:
        
        if isinstance(getattr(money, "io_date", None), str):
            money.io_date = date.fromisoformat(money.io_date)

        db.add(money)
        db.commit()
        db.refresh(money)
        return money

    # PUT
    def update_money(self, id: int, money: MoneyModel, db: Session = Depends(get_db)) -> Optional[MoneyModel]:
        origin = db.get(MoneyModel, id)
        if not origin:
            return None

        origin = self.update_object(origin, money)

        if isinstance(getattr(money, "io_date", None), str):
            money.io_date = date.fromisoformat(money.io_date)

        db.commit()
        db.refresh(origin)
        return origin

    # DELETE
    def delete_money(self, id: int, db: Session = Depends(get_db)) -> bool:
        money = db.get(MoneyModel, id)
        if not money:
            return False
        db.delete(money)
        db.commit()
        return True