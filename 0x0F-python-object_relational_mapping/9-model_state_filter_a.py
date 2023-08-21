#!/usr/bin/python3
"""script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create session
    session = Session()

    # Query first state
    state = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    # display object state
    for states in state:
        print("{}: {}".format(states.id, states.name))

    session.close()
