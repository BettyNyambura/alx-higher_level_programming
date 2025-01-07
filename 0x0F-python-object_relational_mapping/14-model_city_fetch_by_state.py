#!/usr/bin/python3
"""
Fetches and prints all City objects from the database hbtn_0e_14_usa.

The script:
- Connects to a MySQL database using SQLAlchemy.
- Prints each city's ID, name, and associated state's name.
- Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Bind engine and create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to join states and cities and sort by cities.id
    results = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id
    ).order_by(City.id).all()

    # Print results
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close the session
    session.close()
