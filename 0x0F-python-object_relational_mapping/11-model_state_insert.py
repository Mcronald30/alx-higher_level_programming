#!/usr/bin/python3
"""script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""


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

    # create a session
    session = Session()

    # Query and fetch the State object
    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    # display  state
    state = session.query(State).filter(State.name == 'Louisiana').one()
    print(state.id)

    session.close()
