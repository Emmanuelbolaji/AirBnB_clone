#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
import os

class FileStorage:
    """
    Class for serializing instances to a JSON file and deserializing JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

     
    def all(self):
        """
        Returns the dictionary __objects containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the given obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path)
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only reloads if the JSON file (__file_path) exists.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        class_ = eval(class_name)
                        obj = class_.from_dict(value)
                        self.__objects[key] = obj

                except json.JSONDecodeError:
                    pass

    
