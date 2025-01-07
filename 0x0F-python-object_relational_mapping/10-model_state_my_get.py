#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database.

The script:
- Connects to a MySQL database using SQLAlchemy.
- Retrieves and displays the ID of a State object matching the given name.
- If no match is found, displays 'Not found'.
- Takes 4 arguments: mysql username, mysql password, database name,
and state name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Query the State object by name (SQL injection free)
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
