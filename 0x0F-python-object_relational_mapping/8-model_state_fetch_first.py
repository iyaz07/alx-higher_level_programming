#!/usr/bin/python3
""" lists The first object from the database using sqlalchemy"""

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
    First_Element = Session.query(State).first()
    if First_Element is None:
        print("Nothing")
    else:
        print("{}: {}".format(First_Element.id, First_Element.name))
    Session.close()
