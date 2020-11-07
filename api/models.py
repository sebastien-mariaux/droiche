from sqlalchemy import Column, Integer, String
from database import Base, engine

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)            # TODO: should be unique
    left_count = Column(Integer)
    right_count = Column(Integer)
    far_left_count = Column(Integer)
    far_right_count = Column(Integer)

    def __init__(self, content):
        self.content = content
        self.left_count = 0
        self.right_count = 0
        self.far_left_count = 0
        self.far_right_count = 0

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(bind=engine)
