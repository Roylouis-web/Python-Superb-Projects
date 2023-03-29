# AirBnB Clone
### This project combines all the knowledge of both basic to advanced topics of python used to set up the core foundation of the AirBnB Clone
### This includes concepts involved in Object-Oriented Programming:
1. Polymorphism
2. Abstraction
3. Data Encapsulation
4. Inheritance.

#### Some other important concepts used in this project are:
1. Modules - cmd module, json module, os module, shlex module
2. Importing of modules
3. Exceptions in python
4. Unittests
5. Doctests
6. Command line argument
7. Packages and how to create and use them

### The classes involved in the Object-Oriented part of the project are:
- BaseModel: Defines all common attributes/methods for other classes
- User: This class inherits from BaseModel and contains attributes to be used by all users of the website
- State: Inherits from BaseModel and defines all common attribute of a real life state
- City: A subclass of BaseModel that defines all attribute of a city
- Amenity: A subclass of BaseModel that defines all attributes of an amenity
- Place: A subclass of BaseModel that defines all attributes of a place
- Review: A subclass of BaseModel that defines all atrributes of a customer review

### Another core part of the project is "The Console"
The console is built using the python cmd module and is defined with several functions to test the functionality of all the classes in the project
The list of commands handle by the console are:
1. create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Example: $ create BaseModel
2. destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Example: $ destroy BaseModel 1234-1234-1234.
3. update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Example: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
4. show: Prints the string representation of an instance based on the class name and id. Example: $ show BaseModel 1234-1234-1234.
5. all: Prints all string representation of all instances based or not on the class name. Example: $ all BaseModel or $ all.