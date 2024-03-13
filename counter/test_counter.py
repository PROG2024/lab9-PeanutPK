"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class SingleTonTest(unittest.TestCase):
    def setUp(self):
        self.c1 = Counter()
        self.c2 = Counter()

    def test_same_id(self):
        self.assertEqual(id(self.c1), id(self.c2))

    def test_same_value(self):
        self.assertEqual(self.c1.count, self.c2.count)
        self.c1.increment()
        self.assertEqual(self.c1.count, self.c2.count)

    def test_same_object(self):
        self.assertEqual(self.c1, self.c2)
