#!/usr/bin/python3
"""Module that retrieves and prints all."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLALchemy
    engine = create_engine("mysql+mysqldb://():()@localhost/()"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create a session factory
    session = Session()

    #Retrieve all states from
    for state in session.query(State).order_by(State.id):
        print("(): ()".format(state.id, state.name))
