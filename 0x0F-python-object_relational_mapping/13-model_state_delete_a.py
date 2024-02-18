#!/usr/bin/python3
"""
Deletes the State containing 'a'
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and deletes
    a row.name containing 'a'
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_url)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

     # Update record
    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    session.commit()

    # Close session
    session.close()
