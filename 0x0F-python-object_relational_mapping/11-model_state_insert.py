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

    # Create a new State object for 
    louisiana = State(name="Louisiana")
    # Add new state for session
    session.add(louisiana)
    # Commit the session to 
    session.commit()
    # print the ID of the newly added state
    print(louisiana.id)
