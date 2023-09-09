"""
Models for the User and Data Provider objects in the Spike API.
"""
from pydantic import BaseModel


class User(BaseModel):
    """
    A User object, containing information about a user
    """

    user_id: str


class UserIn(User):
    """
    A User object, containing information about a user and the data provider they want to use.
    """

    provider: str


class CallbackUser(User):
    """
    A User object, containing information about a user and the data provider they want to use.
    """

    provider: str
    customer_user_id: str
