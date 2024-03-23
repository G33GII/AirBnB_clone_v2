#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    __abstract__ = True

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        """manage kwargs to create instance attribute from this dictionary"""


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)


    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        storage.new(self)
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """delete the current instance from the storage (models.storage)
        by calling the method delete"""
        from models import storage
        storage.delete(self)