#!/usr/bin/python3
"""
Prints the first State object from the
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and fetch
    first state
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_url)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

   # Query
    State_list = Session.query(State).order_by(State.id)

    for states in State_list:
        print("{}: {}".format(states.id, states.name))
        for city_list in states.cities:
            print("    {}: {}".format(city_list.id, city_list.name))

    Session.close()
