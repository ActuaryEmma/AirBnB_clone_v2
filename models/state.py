#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") != "db":
        name = Column(String(128), nullable=False)

        # Define relationships for DBStorage
        cities = relationship('City', back_populates='state',
                              cascade='all, delete-orphan')


        # Getter att for FileStorage
        # If the env is not HB..- app doesn't use any db for storage this
        # is executed
    @property
    def cities(self):
        """
        Returns a list of city instances with state_id equal to
        current state.id
        """
        cityList = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                cityList.append(city)
            return cityList
