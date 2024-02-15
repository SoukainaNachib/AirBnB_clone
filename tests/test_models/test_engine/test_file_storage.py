#!/usr/bin/python3
"""test file storage"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage class to test the FileStorage class methods.
    """
    def setUp(self):
        """
        Method to set up the test environment.
        Creates an instance of FileStorage.
        """
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Method to clean up after each test.
        Removes the file created by FileStorage if it exists.
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        """Test if new() adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """Test if save() saves objects to the file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        """Check if the file exists and is not empty"""
        str_file_storage = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(str_file_storage))
        self.assertGreater(os.path.getsize(str_file_storage), 0)

    def test_reload(self):
        """Test if reload() reloads objects from the file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        """Create a new storage instance to simulate reloading"""
        new_storage = FileStorage()
        new_storage.reload()

        """ Check if the reloaded object is in the storage"""
        self.assertIn("BaseModel.{}".format(obj.id), new_storage.all())


if __name__ == "__main__":
    unittest.main()
