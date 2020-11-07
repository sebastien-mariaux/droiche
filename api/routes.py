from flask import request
from sqlalchemy import func
from models import Subject
from app import app
from database import SessionLocal


session = SessionLocal()


# @app.route("/subjects/create/", methods=['POST'])
# def create_subject():
#     content = request.form['content']
#     subject = Subject(content)
#     session.add(subject)
#     session.commit()

#     return subject.as_dict()


# @app.route("/subjects/", methods=["GET"])
# def subjects_index():
#     subjects = session.query(Subject).all()
#     return {'subjects': [subject.as_dict() for subject in subjects]}


@app.route("/subjects/<subject_id>/vote/", methods=['POST'])
def vote(subject_id):
    subject = session.query(Subject).get(subject_id)
    vote = request.form['vote']
    if vote == 'left':
        subject.left_count += 1
    elif vote == 'right':
        subject.right_count += 1
    elif vote == 'far_left':
        subject.far_left_count += 1
    elif vote == 'far_right':
        subject.far_right += 1
    session.commit()

    return subject.as_dict()


@app.route("/subjects/random/", methods=["GET"])
def random_subject():
    subject = session.query(Subject).order_by(func.random()).first()
    return subject.as_dict()
