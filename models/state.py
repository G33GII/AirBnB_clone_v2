#!/usr/bin/python3
"""python script"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            city_objs = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
