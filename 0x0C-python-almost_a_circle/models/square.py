#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if kwargs.get("id") is not None:
                self.id = kwargs.get("id")
            if kwargs.get("size") is not None:
                self.size = kwargs.get("size")
            if kwargs.get("x") is not None:
                self.x = kwargs.get("x")
            if kwargs.get("y") is not None:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y

        return dictionary
