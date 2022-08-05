#!/usr/bin/python3
"""python file that contains the class definition of Cities and inherits from
Base located in model_state"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base, State


class City(Base):
    """links to the MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
