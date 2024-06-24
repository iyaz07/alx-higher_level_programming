#!/usr/bin/python3
""" lists all State objects from the database using sqlalchemy"""

import sys
from model_state import Base, State
from model_city import City
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
    query = Session.query(State.name, City.id, City.name)
    query = query.filter(State.id == City.state_id)
    query = query.order_by(City.id)
    Element_list = query.all()

    for element in Element_list:
        print("{}: ({}) {}".format(element[0], element[1], element[2]))
    Session.close()
