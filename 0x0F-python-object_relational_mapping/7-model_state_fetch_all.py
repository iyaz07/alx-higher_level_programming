#!/usr/bin/python3
""" lists all State objects from the database using sqlalchemy"""

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
    Element_list = Session.query(State).order_by(State.id)
    for element in Element_list:
        print("{}: {}".format(element.id, element.name))
    Session.close()
