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
    engine = create_engine(db_url)I
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    query = session.query(State.name, City.id, City.name)
    query = query.filter(State.id == City.state_id)
    query = query.order_by(City.id)
    Element_list = query.all()

    for element in Element_list:
        print("{}: ({}) {}".format(element[0], element[1], element[2]))
    Session.close()
