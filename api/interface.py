from database import SessionLocal
from models import Subject

session = SessionLocal()


def create_subject(text):
    session.add(Subject(content=text))
    session.commit()


def list_subjects():
    for subject in session.query(Subject).all():
        print(subject.content)

