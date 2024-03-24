#!/usr/bin/python3
"""module serializes instances to a JSON file and deserializes JSON file to
instances."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """pass"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        #FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        init_dict = FileStorage.__objects
        new_dict = {key: init_dict[key].to_dict() for key in init_dict.keys()}

        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        """
        try:
            with open(FileStorage.__file_path) as file:
                new_dict = json.load(file)
                for obj in new_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return