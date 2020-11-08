from sqlalchemy import Column, Integer, String
from database import Base, engine

class Subject(Base):
    __tablename__ = 'subjects'
    SERIALIZABLE_FIELDS = [
        'id', 'content', 'right_count', 'left_count', 
        'far_left_count', 'far_right_count', 'votes_count',
        'likes_count', 'dislikes_count']

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)            # TODO: should be unique
    left_count = Column(Integer)
    right_count = Column(Integer)
    far_left_count = Column(Integer)
    far_right_count = Column(Integer)
    likes_count = Column(Integer)
    dislikes_count = Column(Integer)

    def __init__(self, content):
        self.content = content
        self.left_count = 0
        self.right_count = 0
        self.far_left_count = 0
        self.far_right_count = 0
        self.likes_count = 0
        self.dislikes_count = 0

    @property
    def votes_count(self):
        return sum([self.left_count, self.far_left_count, 
         self.far_right_count, self.right_count])

    def thumbs(self, thumb, previous_thumb):
        if thumb == previous_thumb:
            return
        if thumb == 'up':
            self.likes_count += 1
        elif thumb == 'down':
            self.dislikes_count += 1
        if not previous_thumb: 
            return
        if previous_thumb == 'up':
            self.likes_count -= 1
        elif previous_thumb == 'down':
            self.dislikes_count -= 1


    def __repr__(self):
        return self.content

    def as_dict(self):
        return {attr: getattr(self, attr) for attr in self.SERIALIZABLE_FIELDS}

Base.metadata.create_all(bind=engine)
