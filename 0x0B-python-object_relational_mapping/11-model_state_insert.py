#!/usr/bin/python3
'''Adds a State object to a database'''


from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = (State(name='Louisiana'))
    session.add(state_name)
    session.commit()
    print("{}".format(state_name.id))
    session.close()
