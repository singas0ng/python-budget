from fastapi import APIRouter, Depends
from abc import abstractmethod, ABC
from database import get_db
from sqlmodel import Session

class Controller(ABC): #abstract 클래스라는 소리 -> interface랑은 달라서 멤버변수가 있을 수 있음
    def __init__(self, prefix: str):
        self.router = APIRouter(
            prefix=prefix,
            responses={
                404: {
                    "description": "Page Not Found"
                }
            }
        )
    
    @abstractmethod #하위클래스에서 반드시 구현을 하라는 소리
    def _setup_routes(self): # _ 하나면 private or protected
        pass

    def update_object(self, origin, copy) -> object:
        for k, v in copy.__dict__.items():
            if k == "id" or "sa_instance" in k or "reg_date" in k:
                continue
            setattr(origin, k, v)

        return origin