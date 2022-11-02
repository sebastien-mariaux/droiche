from database import SessionLocal
from models import Subject

session = SessionLocal()

initial_subjects = [
    "La pluie",
    "Manger chez Mc Donald",
    "Le Parti Socialiste",
    "La République En Marche",
    "La France Insoumise",
    "Les Républicains",
    "Le Rassemblement national",
    "Le jardinage",
    "Faire grêve",
    "Travailler le 1er mai",
    "Jouer de la cornemuse",
    "L'abstention",
    "Le vote blanc",
    "Le quinquenat",
    "Manger des légumes bio",
    "Respecter le confinement ",
    "Sortir sans masque en période de pandémie",
    "Lire l'Humanité sur la plage de Saint Tropez",
    "Se dire que c'était quand même mieux sous Sarkozy",
    "Un article du 'Figaro' en écriture inclusive",
    "Monter une startup pour lutter contre la précarité",
    "Aller à la Manif Pour Tous avec un T-shirt Che Guevarra",
    "Lire 'Marianne'",
    "Droiche",
    "Marseille",
    "Dénoncer l'islamo-gauchisme",
    "Se plaindre à sa voisine qu'on ne peut plus rien dire de nos jours",
    "Se doucher à l'eau froide",
    "Partir en vacances en Lozère",
    "Voyager en camping-car",
    "Râler parce qu'on paye trop d'impôts",
    "Porter une cravate même le week-end",
]


def create_subject(text: str) -> None:
    session.add(Subject(content=text))
    session.commit()

def create_subjects(subjects: list) -> None:
    for subject in subjects:
        create_subject(subject)


def list_subjects():
    for subject in session.query(Subject).all():
        print(subject.content)


def reset_data():
    session.query(Subject).delete()
    create_subjects(initial_subjects)


def reset_counts():
    session.query(Subject).update({
        Subject.far_left_count: 0, 
        Subject.left_count: 0,
        Subject.right_count: 0,
        Subject.far_right_count: 0,
        Subject.likes_count: 0,
        Subject.dislikes_count: 0 })
    session.commit()
