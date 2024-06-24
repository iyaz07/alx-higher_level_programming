#!/usr/bin/python3
""" list State object containing an 'a' from the database using sqlalchemy"""

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
    a = Session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for element in a:
        print("{}: {}".format(element.id, element.name))
    Session.close()
