#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" in the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create the engine and bind it to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add to the session and commit
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
