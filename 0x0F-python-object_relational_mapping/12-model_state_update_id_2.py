#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa.

The script:
- Connects to a MySQL database using SQLAlchemy.
- Updates the name of the State with id = 2 to "New Mexico".
- Takes 3 arguments: mysql username, mysql password, and database name.
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

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"  # Update the name
        session.commit()  # Commit the changes to the database

    # Close the session
    session.close()
