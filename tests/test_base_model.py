"""
    Module for TestBaseModel
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        A class called TestBaseModel that tests all
        the possible test cases of the BaseModel
    """

    def setUp(self):
        """
            displays a message before the unittest begins
            return: None
        """

        print("Starting unittest")

    def test_plain(self):
        """
            tests for proper output of the attributes
            without the use of *args of **kwargs
            return: None
        """

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertTrue(my_model.id, str)
        self.assertTrue(my_model.created_at, object)
        self.assertTrue(my_model.updated_at, object)
        self.assertTrue(my_model_json['created_at'], str)
        self.assertTrue(my_model_json['updated_at'], str)
        self.assertTrue(my_model_json, dict)

    def test_args_kwargs(self):
        """
            test for correct output when *args and **kwargs
            is given as a parameter
            return: None
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertTrue(my_model.id, str)
        self.assertTrue(my_model.created_at, object)
        self.assertTrue(my_model.updated_at, object)
        self.assertTrue(my_model_json['created_at'], str)
        self.assertTrue(my_model_json['updated_at'], str)
        self.assertTrue(my_model_json, dict)

        self.assertTrue(my_new_model.id, my_model.id)
        self.assertTrue(my_new_model.created_at, object)
        self.assertTrue(my_new_model.updated_at, object)
        self.assertNotEqual(my_model, my_new_model)

    def tearDown(self):
        """
            displays a message after the unittest has ended
            return:
        """

        print("Unittest completed")
