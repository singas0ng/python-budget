from sqlmodel import SQLModel, Field
from datetime import date, datetime
from typing import Optional

from sqlalchemy import Column, Text, VARCHAR, DATE, DATETIME

class Category(SQLModel, table=True):
    __tablename__ = "category"

    id: int                         = Field(primary_key=True, index=True)
    name: str                       = Field(sa_column=Column(comment="카테고리명", type_=VARCHAR), max_length=100)
    description: Optional[str]      = Field(sa_column=Column(type_=Text, comment="카테고리 설명")) # 이렇게 하면 text 형식으로 들어감, @Comment는 이렇게 사용
    # 값이 있을수도 있고 없을수도 있다
    icon: str                       = Field(sa_column=Column(comment="아이콘 파일명", type_=VARCHAR))
    reg_date: datetime              = Field(default=datetime.now(), sa_column=Column(comment="생성일자", type_=DATETIME)) #생성될 때 Field가 null 이면 default 값으로 넣어달라
    modify_date: Optional[datetime] = Field(sa_column=Column(comment="수정일자", type_=DATETIME))