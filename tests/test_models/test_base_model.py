#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class contains unit tests for the BaseModel class.
    """

    def test_init(self):
        """
        Test initialization of BaseModel instance.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """
        Test string representation of BaseModel instance.
        """
        model = BaseModel()
        model_str = str(model)
        self.assertIsInstance(model_str, str)
        self.assertIn("BaseModel", model_str)
        self.assertIn(model.id, model_str)

    def test_save(self):
        """
        Test saving BaseModel instance.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test conversion of BaseModel instance to dictionary.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        key_created_at = model_dict["created_at"]
        value_created_at = model.created_at.isoformat()
        self.assertEqual(key_created_at, value_created_at)
        key_updated_at = model_dict["updated_at"]
        value_updated_at = model.updated_at.isoformat()
        self.assertEqual(key_updated_at, value_updated_at)


if __name__ == "__main__":
    unittest.main()
