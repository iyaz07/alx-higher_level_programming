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

    # Query
    for instance session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(instance.id, instance.name))

    # Close session
    session.close()
