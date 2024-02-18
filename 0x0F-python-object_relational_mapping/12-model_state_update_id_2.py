#!/usr/bin/python3
"""
Update State object id == '2' in
database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and update
    a state
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Initialize engine
    engine = create_engine(db_url)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update record
    update_state = session.query(State).filter(State.id == '2').first()
    update_state.name = 'New Mexico'
    session.commit()

    # Close session
    session.close()
