#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects
from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with their City objects using the relationship
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
