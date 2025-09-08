from .base import Controller
from models.category import Category

from typing import List, Optional

class Category(Controller):
    def __init__(self):
        super().__init__("/category")

    def _setup_routes(self):
        self.router.get("", response_class=List[Category])(self.get_category_list)
        self.router.get("/{id}", response_class=Optional[Category])(self.get_category)
        self.router.post("/{id}", response_class=Optional[Category])(self.create_category)
        self.router.put("/{id}", response_class=Optional[Category])(self.upate_category)
        self.router.delete("/{id}", response_class=bool)(self.delete_category)

    def get_category_list(self) -> List[Category]:
        pass

    def get_category(self, id: int) -> Optional[Category]:
        category = self.db.get(Category, id)

        pass

    def create_category(self, id: int, category: Category) -> Optional[Category]:
        pass

    def upate_category(self, id: int, category: Category) -> Optional[Category]:
        pass

    def delete_category(self, id: int) -> bool:
        pass