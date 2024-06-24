#!/usr/bin/python3
""" lists all State objects from the database using sqlalchemy"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
    New_State = State(name='California')
    New_City = City(name='San Francisco')
    New_State.cities.append(New_City)
    Session.add(New_State)
    Session.add(New_City)
    Session.commit()
    Session.close()
