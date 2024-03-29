#!/usr/bin/python3
""" module lists all State objects with 'a' from database using SQLAlchemy
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    # setup engine
    engine_string = f"mysql://{username}:{passwd}@localhost:3306/{db}"
    # default username: root, passwd: "", db: hbtn_0e_6_usa
    engine = create_engine(engine_string)
    Base.metadata.bind = engine

    # setup session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    list = session.query(State).order_by(State.id).all()
    for elem in list:
        for char in elem.name:
            if char == 'a':
                print(f"{elem.id}: {elem.name}")
                break
