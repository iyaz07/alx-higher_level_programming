#!/usr/bin/python3
"""
Prints the State object from 
argv[4] hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and fetch
    argv[4] as state 
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    instance = session.query(State).filter(State.name == argv[4])

    # Print query
    if instance is None:
        print('Not found')
    else:
        print("{}".format(instance.id))

    # Close session
    session.close()
