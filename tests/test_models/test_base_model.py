#!/usr/bin/python3
import os
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """ Test initialization of BaseModel instance """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_str(self):
         """Test string representation of BaseModel instance"""
         base_model = BaseModel()
         self.assertIsInstance(str(base_model), str)

    def test_save(self):
         """Test if save method updates updated_at attribute"""
         initial_updated_at = base_model.updated_at
         base_model.save()
         self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict(self):
        """ Test conversion of BaseModel instance to dictionary """
        base_model = BaseModel()
        base_model.name = "Test Model"
        base_model.my_number = 42
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['name'], 'Test Model')
        self.assertEqual(base_model_dict['my_number'], 42)



if __name__ == '__main__':
    unittest.main()
