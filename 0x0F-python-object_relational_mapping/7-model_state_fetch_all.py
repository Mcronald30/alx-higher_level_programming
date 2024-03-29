#!/usr/bin/python3
"""Script that lists all State objects
from the database hbtn_0e_6_usa."""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create session
    session = Session()

    # queery first states
    state = session.query(State).order_by(State.id).all()

    # display object states
    for states in state:
        print("{}: {}".format(states.id, states.name))

    session.close()
