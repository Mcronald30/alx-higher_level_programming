#!/usr/bin/python3
"""Improve the files model_city.py and model_state.py
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        return (f"({self.id}) {self.name}");
