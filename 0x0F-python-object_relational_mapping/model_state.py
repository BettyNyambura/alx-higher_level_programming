#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define Base
Base = declarative_base()

# Define State class
class State(Base):
    __tablename__ = 'states'

    # Class attributes representing columns in the table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to the MySQL server running on localhost at port 3306
engine = create_engine(
        'mysql+mysqldb://<username>:<password>@localhost:3306/<dbname>'
)

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
