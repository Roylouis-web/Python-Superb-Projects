"""
    Module for a class called Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        A class called Review that inherits from BaseModel
    """

    place_id = ''
    user_id = ''
    text = ''
