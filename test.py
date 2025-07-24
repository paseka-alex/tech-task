import unittest
import figures

class TestSquare(unittest.TestCase):
    def SetUp():
        pass

    def test_perimeter(self):
        sq = figures.Square(side_length=1, top_right=(1,1))
        self.assertEqual(4, sq.perimeter())

    def test_area(self):
        sq = figures.Square(side_length=1, top_right=(1,1))
        self.assertEqual(1, sq.area())
    
    def test_perimeter2(self):
        sq = figures.Square(side_length=2, top_right=(1,3))
        self.assertEqual(8, sq.perimeter())

    def test_area2(self):
        sq = figures.Square(side_length=2, top_right=(1,3))
        self.assertEqual(4, sq.area())

if __name__ == "__main__":
    unittest.main()