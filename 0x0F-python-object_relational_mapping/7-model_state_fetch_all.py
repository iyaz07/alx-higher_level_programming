#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Print query
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))

    # Close session
    session.close()
