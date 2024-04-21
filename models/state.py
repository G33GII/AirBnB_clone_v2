#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.city import city
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def cities(self):
            """File_storage getter attribute for relationship between state & city"""
            city_objs = []
            for ct in models.storage.all(City).values():
                if ct.state_id == self.id:
                    city_objs.append(ct)
            return city_objs
    else:
        cities = relationship("City", backref="state", cascade="all, delete")
