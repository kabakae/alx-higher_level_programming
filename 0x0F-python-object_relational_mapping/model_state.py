#!/usr/bin/python3
"""Module that defines the states class representing."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL tables to store states.
    id (sqlalchemy.integer): The state's id.
    name (sqlalchemy.String): The state's name."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
