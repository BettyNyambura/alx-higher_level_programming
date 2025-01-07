#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

The script:
- Connects to a MySQL database using SQLAlchemy.
- Retrieves and lists all State objects, ordered by states.id.
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
    
    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()
    
    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
