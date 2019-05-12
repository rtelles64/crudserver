#!/usr/bin/env python3

# Running this file creates a restaurantmenu.db file

# Here we use SQLAlchemy to configure our database
#
# There are 4 major coding components to creating a database with SQLAlchemy:
# 1. Configuration
# 2. Class
# 3. Table
# 4. Mapper

### CONFIGURATION: Beginning of File ###
import sys

from sqlalchemy import Column, ForeignKey, Integer, String  # handy for mapper
# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # to create foriegn key relationships
from sqlalchemy import create_engine  # for configuration at end

Base = declarative_base()  # lets sqlalchemy know that our classes are special
#                            sqlalchemy classes


# CLASS (Contains TABLE and MAPPER code)
class Restaurant(Base):
    # TABLE
    # sqlalchemy syntax: __tablename__ = 'some_table'
    __tablename__ = 'restaurant'

    # MAPPER
    # sqlalchemy syntax: columnName = Column(attributes, ...)
    name = Column(
        String(80),  # 80 character-long string
        nullable=False  # if name not filled out, we cannot create a row
    )

    id = Column(
        Integer,
        primary_key=True
    )

    # SERIALIZE: to help with JSON
    @property
    def serialize(self):
        '''
            Returns object data in easily serializeable format
        '''
        return {
            'name': self.name,
            'id': self.id,
        }


# CLASS
class MenuItem(Base):
    # TABLE
    __tablename__ = 'menu_item'

    # MAPPER
    name = Column(String(80), nullable=False)

    id = Column(Integer, primary_key=True)

    course = Column(String(250))

    description = Column(String(250))

    price = Column(String(8))

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    # sets up relationship between classes
    restaurant = relationship(Restaurant)

    # SERIALIZE: to help with JSON
    @property
    def serialize(self):
        '''
            Returns object data in easily serializeable format
        '''
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


### CONFIGURATION: Insert at end of file ###
# create instance of create_engine class and point to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)  # adds classes to database

# NOTE: The database has been populated with lotsofmenus.py
