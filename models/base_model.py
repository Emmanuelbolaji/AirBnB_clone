#!/usr/bin/python3
"""Module containing BaseModel class
"""


import uuid
import json
from datetime import datetime
import models


class BaseModel:
    """
    A class representing a base model with common attributes/methods for other classes.
    """


    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        If kwargs is provided, initializes the instance with the data from kwargs.
        Otherwise, generates a new unique ID and sets the creation and update timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date and time.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict

    @classmethod
    def from_dict(cls, adict):
        """
        Creates a new instance of BaseModel from a dictionary representation.

        Args:
            adict (dict): A dictionary containing the data to initialize the new instance.

        Returns:
            BaseModel: A new instance of BaseModel initialized with the data from adict.
        """
        return cls(**adict)

    def load_from_file(file_name):
        """
        Loads BaseModel instances from a JSON file.

        Args:
            file_name (str): The name of the JSON file to load the data from.

        Returns:
            lists: A list of BaseModel instances loaded from the JSON file.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                return [BaseModel.from_dict(instance_data) for instance_data in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print(my_model_json)
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    new_model = BaseModel.from_dict(my_model_json)
    print(new_model)
