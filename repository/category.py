from models.category import Category
from .base import BaseRepository as Base
from sqlmodel import Session, select
from typing import Optional, List

class CategoryRepository(Base):
    def __init__(self, db: Session):
        super().__init__(Category, db)

    def getList(self, page: int = 0, count: int = 10) -> List[Category]:
        return self.db.exec(select(Category).offset(page * count).limit(count)).all()

    def create(self, category: Category) -> Category:
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def update(self, id: int, category: Category) -> Category:
        origin = self.db.get(Category, id)
        self.update_object(origin, category)

        self.db.commit()
        self.db.refresh(origin)

        return origin