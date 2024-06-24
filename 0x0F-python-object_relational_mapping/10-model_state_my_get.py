#!/usr/bin/python3
""" Gets the Id of a searched State from the database using sqlalchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    UN = sys.argv[1]
    PW = sys.argv[2]
    DB = sys.argv[3]
    link = 'mysql+mysqldb://{}:{}@localhost:3366/{}'.format(UN, PW, DB)
    engine = create_engine(link)
    Base.metadata.create_all(engine)
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    state_id = Session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(state_id[0].id)
    except IndexError:
        print("Not found")
    Session.close()
