"""
    Module for a class called TestFileStorage
"""

import unittest
import os
import re
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
        A class called TestFileStorage that tests all
        possible test cases of the FileStorage class
    """

    def setUp(self):
        """
            displays a message before the unittest begins
            return: None
        """

        print("Starting unittest")

    def test_methods(self):
        """
            Tests for correct output of the methods
            pf FileStorage
            return: None
        """

        my_model = BaseModel()
        storage.new(my_model)
        dict_obj = storage.all()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        for value in dict_obj.values():
            self.assertTrue(value, object)
        self.assertTrue(dict_obj, dict)

    def tearDown(self):
        """
            displays a message after the unittest has ended
            return:
        """

        print("Unittest completed")
