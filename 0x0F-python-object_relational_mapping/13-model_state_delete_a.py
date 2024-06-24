#!/usr/bin/python3
""" Deletes any State that has 'a' in database using sqlalchemy"""
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
    a = Session.query(State).filter(State.name.like('%a%'))
    for element in a:
        Session.delete(element)
    Session.commit()
    Session.close()
