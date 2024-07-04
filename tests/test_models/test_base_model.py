#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down test methods"""
        pass

    def test_instantiation(self):
        """Test instantiation of BaseModel class"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id_is_string(self):
        """Test if id is a string"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method"""
        string = str(self.base_model)
        self.assertIn("[BaseModel]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_instantiation_with_kwargs(self):
        """Test instantiation with kwargs"""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)                                                      self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args(self): 
        """Test that instantiation with args works correctly"""
        bm = BaseModel("1234", "Hello")                                                                                     self.assertNotIn("1234", bm.__dict__.values())
        self.assertNotIn("Hello", bm.__dict__.values())

    def test_instantiation_with_kwargs_and_args(self):



if __name__ == '__main__':
    unittest.main()
