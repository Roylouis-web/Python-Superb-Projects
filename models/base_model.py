"""
    Module for a class called BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel(object):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])

            for key in kwargs.keys():
                self.__setattr__(key, kwargs[key])

    def __str__(self):
        """
        A representation of the object
        return: A string
        """

        class_name = self.__class__.__name__
        _id = self.id
        dic = self.__dict__

        return '[{}] ({}) {}'.format(class_name, _id, dic)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        return: None
        """

        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance:
        return: A dictionary
        """

        dic = self.__dict__
        class_name = self.__class__.__name__
        temp = dic.copy()

        if '__class__' not in temp:
            temp['__class__'] = class_name
        temp['created_at'] = datetime.isoformat(temp['created_at'])
        temp['updated_at'] = datetime.isoformat(temp['updated_at'])
        return temp
