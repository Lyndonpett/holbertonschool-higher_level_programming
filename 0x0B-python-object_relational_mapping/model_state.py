#!/bin/usr/python3
'''This module defines class State'''


from sqlalchemy import Column, Index, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer

Base = declarative_base()


class State(Base):
    '''Defining class State'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
