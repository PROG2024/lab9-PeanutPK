"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math
import unittest

from circle import Circle


class Test(unittest.TestCase):
    """Test add area function in circle and invalid radius input"""

    def test_add_area(self):
        """Test normal area adding for Circle object with radius 2 and 4"""
        # math.hypot(x, y) returns sqrt(x*x + y*y)
        rad = math.hypot(2, 4)
        self.assertTrue(rad == Circle(2).add_area(Circle(4)).radius)

    def test_add_area_zero(self):
        """Try edge case with one of them has zero as radius"""
        rad = math.hypot(0, 4)
        self.assertTrue(rad == Circle(0).add_area(Circle(4)).radius)

    def test_negative_radius(self):
        """Invalid negative value input for Circle object"""
        with self.assertRaises(ValueError):
            Circle(-1)  # try input an invalid negative number of -1


if __name__ == '__main__':
    start = Test()
    start.run()
