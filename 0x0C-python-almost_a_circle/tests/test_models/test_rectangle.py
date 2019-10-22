#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init_rectangle(self):

        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)
        with self.assertRaises(TypeError):
            r1 = Rectangle("d")

    def test_getters_setters(self):

        self.assertEqual(Rectangle(10, 10).height, 10)
        self.assertEqual(Rectangle(10, 10).width, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.width, 10)
        r3.width = 1
        self.assertEqual(r3.width, 1)
        r3.height = 9
        self.assertEqual(r3.height, 9)
        r3.x = 2
        self.assertEqual(r3.x, 2)
        r3.y = 1
        self.assertEqual(r3.y, 1)
        
    def test_validate_attributes(self):

        with self.assertRaises(TypeError):
            r4 = Rectangle("w", 10)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "g")
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 10)
            r4.width = "w"
        with self.assertRaises(TypeError):
            r4.height = "h"
        with self.assertRaises(TypeError):
            r4.x = "x"
        with self.assertRaises(TypeError):
            r4.y = "y"
        with self.assertRaises(TypeError):
             r = Rectangle(10, 2)
             r.x = {}


    def test_validate_values_attributes(self):
        r4 = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            r4.x = -1
        with self.assertRaises(ValueError):
            r4.y = -1
        with self.assertRaises(ValueError):
            r4.width = 0
        with self.assertRaises(ValueError):
            r4.height = 0
        with self.assertRaises(TypeError):
            r4.x = 100.8
        with self.assertRaises(TypeError):
            r4.x = float('nan')
        with self.assertRaises(TypeError):
            r4.x = float(10E1000)
        with self.assertRaises(TypeError):
            r4.x = (4,)
       
        with self.assertRaises(TypeError):
            r4.x = [3]
        with self.assertRaises(TypeError):
            r4.x = True
        with self.assertRaises(TypeError):
            r4.x = {3, 4}
        with self.assertRaises(TypeError):
            r4.x = None

        with self.assertRaises(TypeError):
            r4.y = 100.8
        with self.assertRaises(TypeError):
            r4.y = float('nan')
        with self.assertRaises(TypeError):
            r4.y = float(10E1000)
        with self.assertRaises(TypeError):
            r4.y = (4,)

        with self.assertRaises(TypeError):
            r4.y = [3]
        with self.assertRaises(TypeError):
            r4.y = True
        with self.assertRaises(TypeError):
            r4.y = {3, 4}
        with self.assertRaises(TypeError):
            r4.y = None

        with self.assertRaises(TypeError):
            r4.height = 100.8
        with self.assertRaises(TypeError):
            r4.height = float('nan')
        with self.assertRaises(TypeError):
            r4.height = float(10E1000)
        with self.assertRaises(TypeError):
            r4.height = (4,)

        with self.assertRaises(TypeError):
            r4.height = [3]
        with self.assertRaises(TypeError):
            r4.height = True
        with self.assertRaises(TypeError):
            r4.height= {3, 4}
        with self.assertRaises(TypeError):
            r4.height = None




        with self.assertRaises(TypeError):
            r4.width = 100.8
        with self.assertRaises(TypeError):
            r4.width = float('nan')
        with self.assertRaises(TypeError):
            r4.width = float(10E1000)
        with self.assertRaises(TypeError):
            r4.width = (4,)

        with self.assertRaises(TypeError):
            r4.width = [3]
        with self.assertRaises(TypeError):
            r4.width = True
        with self.assertRaises(TypeError):
            r4.width = {3, 4}
        with self.assertRaises(TypeError):
            r4.width = None





    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_display(self):
        r1 = Rectangle(2, 2)


    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        

        with self.assertRaises(ValueError):
            r1.update(1, -2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.update(1, "c", 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.update(1, {}, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.update(1, 100.8, 9, 9)
        with self.assertRaises(TypeError):
            r1.update(1, float('nan'), 9, 9)
        with self.assertRaises(TypeError):
            r1.update(1, float(10E1000), 9, 9)
        with self.assertRaises(TypeError):
            r1.update(1, (4,), 9, 9)
        with self.assertRaises(TypeError):
            r1.update(1, [3], 9, 9)
        with self.assertRaises(TypeError):
            r1.update(1, True, 9, 9)
        with self.assertRaises(TypeError):
            r1.update(1, None, 9, 9)



        with self.assertRaises(ValueError):
            r1.update(1, 2, -3, 4, 5)
        with self.assertRaises(TypeError):
            r1.update(1, 2, "3", 4, 5)
        with self.assertRaises(TypeError):
            r1.update(1, 3, {}, 4)
        with self.assertRaises(TypeError):
            r1.update(1, 9, 100.8, 9)
        with self.assertRaises(TypeError):
            r1.update(1, 9, float('nan'), 9)
        with self.assertRaises(TypeError):
            r1.update(1, 9, float(10E1000), 9)
        with self.assertRaises(TypeError):
            r1.update(1, 9, (4,), 9)
        with self.assertRaises(TypeError):
            r1.update(1, 9, [3], 9)
        with self.assertRaises(TypeError):
            r1.update(1, 9, True, 9)
        with self.assertRaises(TypeError):
            r1.update(1, 9, None, 9)





    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height = 1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        with self.assertRaises(ValueError):
            r1.update(height = -1)
        with self.assertRaises(TypeError):
            r1.update(height = "i")
        with self.assertRaises(TypeError):
            r1.update(height = {})
        with self.assertRaises(TypeError):
            r1.update(height = 100.8)
        with self.assertRaises(TypeError):
            r1.update(height = float('nan'))
        with self.assertRaises(TypeError):
            r1.update(height = float(10E1000))
        with self.assertRaises(TypeError):
            r1.update(height = (4,))
        with self.assertRaises(TypeError):
            r1.update(height = [3])
        with self.assertRaises(TypeError):
            r1.update(height = True)



if __name__ == "__main__":
    unittest.main()
