#!/usr/bin/python3
"""
Module to define the State class and connect to the MySQL database

This script connects to a MySQL database using SQLAlchemy and lists all
State objects (rows) from the `states` table, ordered by `id`. The script
requires the following command-line arguments:
1. MySQL username
2. MySQL password
3. Database name

The results are printed in ascending order by the `id` field of the `states`
table. This script uses the SQLAlchemy library for interacting with the
MySQL database.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define Base
Base = declarative_base()

# Define State class
class State(Base):
    """State class that represents the 'states' table in the database"""
    __tablename__ = 'states'

    # id column: auto-incremented, unique, primary key, non-nullable
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # name column: non-nullable string with a max length of 128 characters
    name = Column(String(128), nullable=False)

# Connect to the MySQL server running on localhost at port 3306
engine = create_engine('mysql+mysqldb://<username>:<password>@localhost:3306/<dbname>')

# Create all tables (State class must be imported before this call)
Base.metadata.create_all(engine)

# Session setup (optional if you want to interact with the database)
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a state (uncomment to test)
# new_state = State(name="California")
# session.add(new_state)
# session.commit()

# Close the session
session.close()
