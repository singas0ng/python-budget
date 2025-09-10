from sqlmodel import SQLModel, Field # SQLAlchemy -> python에서 sql을 ORM 처럼 사용할수 있게 해줌
from datetime import date, datetime
from typing import Optional

from sqlalchemy import Column, Text, VARCHAR, DATETIME, DATE, INTEGER

from models.category import Category
from pydantic import field_validator

class Money(SQLModel, table=True):
    __tablename__ = "money"

    id: int                         = Field(primary_key=True, index=True)
    money_type: str                 = Field(sa_column=Column(comment="입/출금 구분", type_=VARCHAR))
    value: int                      = Field(sa_column=Column(comment="금액", type_=VARCHAR))
    category: Category              = Field(foreign_key="category.id", sa_type=INTEGER)
    description: str                = Field(sa_column=Column(comment="설명", type_=Text))
    io_date: date                   = Field(sa_column=Column(comment="입/출금 일자", type_=DATE))
    reg_date: datetime              = Field(sa_column=Column(comment="생성일자", type_=DATETIME), default=datetime.now()) #생성될 때 Field가 null 이면 default 값으로 넣어달라
    modify_date: Optional[datetime] = Field(sa_column=Column(comment="수정일자", type_=DATETIME))