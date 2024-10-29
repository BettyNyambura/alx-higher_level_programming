#!/usr/bin/python3

""" Defines The class Base module"""


class Base:

    """Represents the base model.

    This class manages 'id' attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        """
        initialize base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
