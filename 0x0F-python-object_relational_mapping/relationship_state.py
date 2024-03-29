#!/usr/bin/python3
"""State class definition that inherits from Base"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(256), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
