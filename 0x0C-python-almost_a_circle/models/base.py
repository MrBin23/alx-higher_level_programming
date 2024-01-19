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
    def __init__(self, id=None):

    """
    initialise instance with unique id

    Args:
    id (int, optional): the id value to assign the instance
    """

        if id is not None:
            self.id = id
            # Increment the class counter __nb_objects
        else:
            Base.__nb_objects += 1
            # Assign the new value of __nb_objects to the public instance attribute 'id'
            self.id = Base.__nb_objects
