#!/usr/bin/python3
class Base:
    """
    Base class for managing id attributes in all future classes

    Attributes:
    __nb_objects (int): counter for number of instance created

    Method:
    __init__(self, id=None): class constructor to initialize the instance with id
    """
    __nb_objects = 0
    """
    initialise instance with unique id

    Args:
    id (int, optional): the id value to assign the instance
    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
