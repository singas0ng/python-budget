from .base import Controller

from fastapi import Depends
from typing import List, Optional
from datetime import datetime

from sqlmodel import Session, select

from models.category import Category as CategoryModel
from database import get_db


class CategoryController(Controller):
    def __init__(self):
        super().__init__("/category")
        self._setup_routes()

    def _setup_routes(self):
        self.router.get("", response_model=List[CategoryModel])(self.get_category_list)
        self.router.get("/{id}", response_model=Optional[CategoryModel])(self.get_category)
        self.router.post("", response_model=CategoryModel)(self.create_category)
        self.router.put("/{id}", response_model=Optional[CategoryModel])(self.update_category)
        self.router.delete("/{id}", response_model=bool)(self.delete_category)

    # GET
    def get_category_list(self, db: Session = Depends(get_db)) -> List[CategoryModel]:
        results = db.exec(select(CategoryModel)).all()
        return results

    def get_category(self, id: int, db: Session = Depends(get_db)) -> Optional[CategoryModel]:
        category = db.get(CategoryModel, id)
        return category

    # POST
    def create_category(self, category: CategoryModel, db: Session = Depends(get_db)) -> CategoryModel:
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    # PUT
    def update_category(self, id: int, category: CategoryModel, db: Session = Depends(get_db)) -> Optional[CategoryModel]:
        origin = db.get(CategoryModel, id)
        if not origin:
            return None

        origin = self.update_object(origin, category)

        db.commit()
        db.refresh(origin)
        return origin

    # DELETE
    def delete_category(self, id: int, db: Session = Depends(get_db)) -> bool:
        category = db.get(CategoryModel, id)
        if not category:
            return False
        db.delete(category)
        db.commit()
        return True