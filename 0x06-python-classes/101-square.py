#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):

            self.size = size
            self.position = position

    def area(self):
            return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        try:
            int(position[0])
            int(position[1])
        except:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(position[0], int) and isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        if self.size == 0:
            print()
            return
        if self.position[1] == 1:
            for k in range(self.position[1]):
                print()
        for i in range(self.size):
            for t in range(self.position[0]):
                    print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

    def __str__(self):
        line = list()
        if self.size == 0:
            return "".join(line)

        for k in range(self.position[1]):
                line.append("\n")
        for i in range(self.size):
            for t in range(self.position[0]):
                    line.append(" ")
            for j in range(self.size):
                line.append("#")
            line.append("\n")
        line.pop()
        return "".join(line)
