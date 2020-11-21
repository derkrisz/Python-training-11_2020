import unittest

from my_point import Point

class TestPoint(unittest.TestCase):
   
    def setUp(self):
        self.point = Point(3, 5)

    def test_move_by(self):
        self.point.move_by(5, 2)
        self.assertEqual(self.point.where_am_i(), 'Point at 8, 7')


if __name__ == '__main__':
    unittest.main()