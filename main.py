from fastapi import FastAPI

from database import engine
from sqlmodel import SQLModel

from fastapi.middleware.cors import CORSMiddleware

from controller.category import CategoryController
from controller.money import MoneyController

SQLModel.metadata.create_all(bind=engine) #Enity를 가지고 table을 만든다 (SqlModel을 상속받은 얘들만)

app = FastAPI()

########### Routes ########### 

category = CategoryController()
money = MoneyController()

app.include_router(category.router)
app.include_router(money.router)

########### Routes ###########

'''
브라우저에서 http 요쳥을 하면 서버로 들어오고 Router(Controller) 로 가서 쭉쭉 들어가서 로직구현하고 나서 
다시 Controller 거치고 서버 거쳐서 httpResponse로 브라우저한테 다시 넘김

Browser -> HTTP -> Server -> Middleware -> Router(Controller) -> Logic
        <-      <-        <-            <-                    <-

미들웨어는 서버랑 라우터 사이 들어감
'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'], # 요청하는 포트 (브라우저가 서버로 요청을 하니까 브라우저 포트 적기)
    allow_credentials=True, # header 에 토큰 허용해주는거
    allow_methods=['*'], # GET POST PUT DELETE
    allow_headers=['*']
)



# @app.get("/category/{id}")
# def get_category(id: int, db: Session = Depends(get_db)) -> Optional[Category]:

#     # stat = select(Category).where(Category.id == id).order_by(Category.id) -> 아이디 하나만 가지고 오는데 이렇게 쓸 필요가 있을까?
#     # category = db.exec(stat).first()
#     # return category[0] 
#     category = db.get(Category, id) # pk를 가지고 올때는 이렇게 작성함
    
#     # print(category) -> 이렇게 하면 결과가 tuple이 나옴

#     return category #Category를 Optional 로 묶어서 if문 필요 X

# @app.post("/category")
# def create_category(category: Category, db: Session = Depends(get_db)): #의존성주입을 통해 Session을 매번 새로 만들필요 없게끔 함
#     db.add(category)
#     db.commit()

#     return category


# @app.put("/category/{id}")
# def update_category(id: int, category: Category, db: Session = Depends(get_db)):
#     origin_category = db.get(Category, id) # db를 참조해서 직접 가져온거라서 session 정보가 있는데 위에 body로 가져온거는 session 정보 없음

#     # 이거는 밑으로 빼서 함수로 만들어주고 호출하기
#     # for k,v in category.__dict__.items():  # k, v가 위에서 가져온 category의 key, value
#     #     if k == "id" or "sa_instance" in k:
#     #         continue
#     #     setattr(origin_category, k, v) # 가져온거를 origin_category에 setAttribute를 통해 넣어줌

#     # origin_category.modify_date = datetime.now()

#     origin_category = update_object(origin_category, category)

#     db.commit()
#     db.refresh(origin_category)

#     return origin_category

# @app.delete("/category/{id}")
# def delete_category(id: int, db: Session = Depends(get_db)):
#     category = db.get(Category.id)
#     db.delete(category)

#     db.commit()

#     return True


# def update_object(origin, modified):
#     for k,v in modified.__dict__.items():
#         if k == "id" or "sa_instance" in k:
#             continue
#         setattr(origin, k, v)

#     origin.modify_date = datetime.now()

#     return origin

