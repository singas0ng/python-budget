from pydantic import BaseModel

class Human(BaseModel):
    name: str
    age: int
    height: int
    weight: int
    gender: str

class Man(Human):
    name: str


class Woman(Human):
    name: str