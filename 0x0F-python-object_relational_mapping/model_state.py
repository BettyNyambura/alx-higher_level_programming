#!/usr/bin/python3
"""Module that defines the State class for the 'states' table in the db"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import City

Base = declarative_base()


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'

    # Primary key: unique, auto-incremented, non-nullable
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)

     # Name of the state: non-nullable string with max length of 128 chars
    name = Column(String(128), nullable=False)
