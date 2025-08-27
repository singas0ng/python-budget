from fastapi import FastAPI
from dto import Human
from typing import Dict, Any


app = FastAPI()


@app.get("/")
def main(name: str = ""):
    return {
        "name": name,
        "message": "Hello, World"
    }

@app.get("/{name}")
def print_name(name: str, age: int = 0):
    return {
        "name": name,
        "age": age
    }

#@app.post("/")
#def post_body(human: Human):
#    return {
#        "message": f"Hello, {human.name}!"
#    }


@app.post("/")
def post_body(human: Human) -> Human:
        # -> Human 이 return type 이라는 것
#def post_body(human: Human) -> Dict:
# -> 이거는 Dict 으로 return
# 이렇게 하면 근데 오류남.. Human은 dto 라 Dict랑 type이 다름
    return human

@app.post("/")
def post_body(human: Human) -> Dict:
    return human.__dict__
# 이렇게 하면 모든 클래스가 Dict으로 바껴서 나옴
# Human 클래스는 BaseModel을 상속받고 있는데 BaseModel 들어가면 dict가 있음
# -> 그래서 return human.model_dump() 해도 Dict로 나옴

@app.post("/{id}")
def post_body(human: Human, id: int) -> Dict:
    result = {
        "id": id,
        "name": "1234"
        # key는 중복이 안되기 때문에 Human 안에 있는 name이 덮어씀
    }

    human_data = human.model_dump()

    #result 안에 human_data 가 병합되서 나옴
    result.update(human_data)

    return result

