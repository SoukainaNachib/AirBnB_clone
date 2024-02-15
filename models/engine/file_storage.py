#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone.
Module: file_storage.py
Defines a `FileStorage` class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances.
    __file_path: path to the JSON file.
    __objects: objects will be stored.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        current_classes = {
                'BaseModel': BaseModel,
                'user': User,
                'Amenity': Amenity,
                'City': City,
                'State': State,
                'Place': Place,
                'Review': Review
                }
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj = eval(cls_name)(**val)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
