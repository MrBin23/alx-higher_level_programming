0x0C. Python - Almost a circle

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


1. Base class
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
