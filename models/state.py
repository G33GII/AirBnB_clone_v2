#!/usr/bin/python3
""" State Module for HBNB project """
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
            city_objs = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
    else:
        cities = relationship("City", back_populates="state",
                              cascade="all, delete, delete-orphan")
