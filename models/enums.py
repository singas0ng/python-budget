from pydantic import BaseModel
from enum import Enum
from datetime import date, datetime

# Enumeration: 열거형

class MoneyType(Enum):
    INCOME = 0 #static -> compile 타임에 힙영역에 저장됨
    SPEND = 1
