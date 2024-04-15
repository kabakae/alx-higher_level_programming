#!/usr/bin/python3
"""Module that retrieves and prints all."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLALchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a session factory
    Session = sessionmaker(bind=engine)

    session = Session()
    # Retrive the state with id
    state = session.query(State).filter_by(id=2).first()
    # update name of the state
    state.name = "New Mexico"
    # Commit the session
    session.commit()
