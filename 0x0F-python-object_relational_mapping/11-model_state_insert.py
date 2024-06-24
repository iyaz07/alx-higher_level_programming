#!/usr/bin/python3
""" Adds a new State and prints it id after in database using sqlalchemy"""
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
    New_state = State(name='Louisiana')
    Session.add(New_state)
    state_id = Session.query(State).filter_by(name='Louisiana').first()
    print(state_id.id)
    Session.commit()
    Session.close()

