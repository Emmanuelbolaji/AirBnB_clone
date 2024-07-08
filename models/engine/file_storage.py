#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass
