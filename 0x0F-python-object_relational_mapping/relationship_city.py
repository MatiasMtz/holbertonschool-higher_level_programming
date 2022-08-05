#!/usr/bin/python3
"""python file that contains the class definition of Cities and inherits from
Base located in relationship_state"""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """links to the MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
