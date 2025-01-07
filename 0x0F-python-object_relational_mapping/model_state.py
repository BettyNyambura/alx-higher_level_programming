#!/usr/bin/python3
"""
Defines a State class and an instance Base = declarative_base().

State class:
- Inherits from Base.
- Links to the MySQL table `states`.
- Has id and name attributes:
  * id: auto-generated, unique integer, primary key, not null.
  * name: string with max 128 characters, not null.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
