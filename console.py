"""
    Module for a class called HBNBCommand
"""

import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        A class called HBNBCommand  that contains the entry
        point of the command interpreter:
    """

    intro = "Welcome to Le Roy's Console"
    prompt = '(hbnb) '
    classes = [
        'BaseModel', 'User', 'State',
        'City', 'Amenity', 'Place', 'Review'
    ]

    @staticmethod
    def do_quit(line):
        """Quit command to exit the program"""

        exit()

    @staticmethod
    def do_EOF(line):
        """Implements EOF"""

        return True

    @staticmethod
    def do_create(line):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """

        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            my_model = eval(line)()
            print(my_model.id)
            my_model.save()

    @staticmethod
    def help_create():
        """Helps with the docs of create command"""
        print('\n'
              .join(
                ['Creates a new instance of BaseModel',
                 'saves it (to the JSON file) and prints the id']))

    @staticmethod
    def do_show(line):
        """
            Prints the string representation of an
            instance based on the class name and id
        """

        arr = line.split()
        objects = storage.all()
        if len(arr) == 0:
            print('** class name missing **')
        elif arr[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(arr[0], arr[1])
            value = objects.get(key)
            if value is None:
                print('** no instance found **')
            else:
                print(value)

    @staticmethod
    def help_show():
        """Helps with the docs of show command"""

        print('\n'
              .join(
                [
                    'Prints the string representation of an',
                    'instance based on the class name and id'
                ]))

    @staticmethod
    def do_destroy(line):
        """
            Deletes an instance based on the class name and
            id (save the change into the JSON file)
        """

        arr = line.split()
        objects = storage.all()
        if len(arr) == 0:
            print('** class name missing **')
        elif arr[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(arr[0], arr[1])
            value = objects.get(key)
            if value is None:
                print('** no instance found **')
            else:
                del objects[key]
                storage.save()

    @staticmethod
    def help_destroy():
        """Helps with the docs of destroy command"""

        print('\n'
              .join(
                ['Deletes an instance based on the class name and',
                 'id (save the change into the JSON file)']))

    @staticmethod
    def do_all(line):
        """
            Prints all string representation of all
            instances based or not on the class name
        """

        objects = storage.all()
        if line:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in objects.items():
                    if value.to_dict()['__class__'] == line:
                        print(value)
        else:
            for key, value in objects.items():
                print(value)

    @staticmethod
    def help_all():
        """Helps the docs of the all command"""

        print('\n'
              .join(['Prints all string representation of all',
                     'instances based or not on the class name']))

    @staticmethod
    def do_update(line):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file)
        """

        arr = line.split()
        objects = storage.all()
        if len(arr) == 0:
            print('** class name missing **')
        elif arr[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arr) == 1:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(arr[0], arr[1])
            value = objects.get(key)
            if value is None:
                print('** no instance found **')
            else:
                attribute = arr[2]
                num = HBNBCommand.check(arr[3])
                value.__setattr__(attribute, num)
                storage.save()

    @staticmethod
    def help_update():
        """Helps the docs of the update command"""

        print('\n'
              .join(['Updates an instance based on the class name',
                     'and id by adding or updating attribute',
                     '(save the change into the JSON file)']))

    @staticmethod
    def do_create_all(line):
        """
            Creates instances of all the class available
            In the order BaseModel, User, State, City, Amenity
            Place, Review
        """

        arr = line.split()

        match len(arr):
            case 0:
                print('class name: BaseModel, User, State, City, Amenity, Place, Review missing')
            case 1:
                print('class name: User, State, City, Amenity, Place, Review missing')
            case 2:
                print('class name: State, City, Amenity, Place, Review missing')
            case 3:
                print('class name: City, Amenity, Place, Review missing')
            case 4:
                print('class name: Amenity, Place, Review missing')
            case 5:
                print('class name: Place, Review missing')
            case 6:
                print('class name: Review missing')
            case default:
                for class_name in arr:
                    if class_name not in HBNBCommand.classes:
                        print("one or more of the class names doesn't exist")
                        exit()
                    else:
                        new = eval(class_name)()
                        print(new.id)
                        new.save()

    def default(self, line):
        arr = line.split('.')
        if arr[0] in self.classes and arr[1] == 'all()':
            self.do_all(arr[0])
        elif arr[0] in self.classes and arr[1] == 'count()':
            count = 0
            objects = storage.all()
            if arr[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in objects.items():
                    if value.to_dict()['__class__'] == arr[0]:
                        count += 1
            print(count)
        elif arr[0] in self.classes and re.match('show', arr[1]):
            new = arr[1].split('(')
            final = new[1].split(')')
            first = arr[0]
            third = final[0]

            HBNBCommand.do_show(f'{first} {third}')
        elif arr[0] in self.classes and re.match('destroy', arr[1]):
            new = arr[1].split('(')
            final = new[1].split(')')
            first = arr[0]
            third = final[0]

            HBNBCommand.do_destroy(f'{first} {third}')
        elif arr[0] in self.classes and re.match('update', arr[1]):
            try:
                objects = storage.all()
                class_name = arr[0]
                dic = eval(line[50:-1])
                trans = arr[1].split(', ')
                trans2 = trans[0].split('(')
                _id = trans2[1]
                args = [class_name, _id, dic]
                if len(args) == 0:
                    print('** class name missing **')
                elif class_name not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print('** instance id missing **')
                elif len(args) == 2:
                    print('** dictionary missing **')
                else:
                    key = "{}.{}".format(class_name, _id)
                    print(class_name, _id)
                    value = objects.get(key)
                    if value is None:
                        print('** no instance found **')
                    else:
                        for key in dic.keys():
                            value.__setattr__(key, dic[key])
                        storage.save()
            except:
                arr = line.split('.')
                class_name = arr[0]
                stage1 = arr[1].split('(')
                new = stage1[1].split(')')
                new2 = new[0].split(',')
                _id, attr_name, attr_value = new2
                self.do_update(f'{class_name} {_id} {attr_name} {attr_value}')

    @staticmethod
    def check(num):
        if num.isnumeric():
            num = int(num)
        else:
            try:
                num = float(num)
            except ValueError:
                pass
        return num


if __name__ == '__main__':
    HBNBCommand().cmdloop()
