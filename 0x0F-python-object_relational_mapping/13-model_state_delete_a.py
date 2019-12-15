#!/usr/bin/python3
'''script that deletes all State objects with a name containing the letter a'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    d = State.__table__.delete().where(State.name.like('%ES%'))
    engine.execute(d)
