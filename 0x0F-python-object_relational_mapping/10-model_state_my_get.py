#!/usr/bin/python3
'''
script that prints the State object with the name passed as argument
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(engine)

    session = Session()
    try:
        instance = session.query(State).filter(State.name == sys.argv[4]).one()
        print("{}".format(instance.id))
    except NoResultFound:
        print("Not found")
