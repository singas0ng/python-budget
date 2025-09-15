from sqlmodel import Session, select
from typing import Optional, List

class BaseRepository:
    def __init__(self, clazz, db: Session):
        self.clazz = clazz
        self.db = db
    
    def getById(self, id: int) -> Optional[object]: #자바 object랑 같음
        return self.db.get(self.clazz, id)
    
    def update_object(self, origin, copy) -> object:
        for k, v in copy.__dict__.items():
            if k == "id" or "sa_instance" in k or "reg_date" in k:
                continue
            setattr(origin, k, v)
        return origin
    
    def delete_list(self, id: int) -> bool:
        origin = self.getById(id)

        if not origin:
            return False

        self.db.delete(origin)
        self.db.commit()

        return True

    def deleteByIdList(self, id_list: List[int]) -> bool:
        if not id_list:
            return False
        
        origins = self.db.exec(select(self.clazz).where(self.clazz.id.in_(id_list))).all()

        if not origins:
            return False
        
        for origin in origins:
            self.db.delete(origin)

        self.db.commit()

        return True