# sqlite 사용 -> 서버없이 로컬에 파일로 db를 저장
from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///database.db")

# Session 만들려고 생성
def get_db():
    with Session(engine) as session:
        yield session