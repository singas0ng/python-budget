from fastapi import FastAPI, Depends
from typing import Dict, List

from database import engine, get_db
from sqlmodel import SQLModel, Session, select

from sqlalchemy import select

from models.category import Category
from models.money import Money

SQLModel.metadata.create_all(bind=engine) #Enity를 가지고 table을 만든다 (SqlModel을 상속받은 얘들만)

app = FastAPI()

@app.get("/category/{id}")
def get_category(id: int, db: Session = Depends(get_db)) -> List[Category]:

    stat = select(Category).where(Category.id  == id).order_by(Category.id)

    category = db.exec(stat).all()

    return category

@app.post("/category")
def create_category(category: Category, db: Session = Depends(get_db)): #의존성주입을 통해 Session을 매번 새로 만들필요 없게끔 함
    db.add(category)
    db.commit()

    return category