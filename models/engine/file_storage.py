"""
    Module for a class called FileStorage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage(object):
    """
        a class FileStorage that serializes instances to a JSON
        file and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """

        temp = FileStorage.__objects
        class_name = obj.__class__.__name__
        _id = obj.id
        string = "{}.{}".format(class_name, _id)
        temp.update({string: obj})

    def save(self):
        """
           serializes __objects to the
           JSON file (path: __file_path)
        """

        temp = {}
        file = FileStorage.__file_path
        for key, value in FileStorage.__objects.items():
            temp.update({key: value.to_dict()})
        with open(file, mode='w', encoding='utf8') as f:
            f.write(json.dumps(temp))

    def reload(self):
        """
            deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """

        file = FileStorage.__file_path
        temp = {}
        new = FileStorage.__objects
        try:
            with open(file, mode='r', encoding='utf8') as f:
                temp.update(json.loads(f.read()))
        except FileNotFoundError:
            pass

        for k, v in temp.items():
            new.update({k: eval(v['__class__'])(**v)})
