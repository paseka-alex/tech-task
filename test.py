import unittest
import figures

class TestSquare(unittest.TestCase):
    def SetUp():
        pass

    def test_Perimeter(self):
        sq = figures.Square(side_length=1, top_right=(1,1))
        self.assertEqual(4, sq.perimeter())

    def test_area(self):
        sq = figures.Square(side_length=1, top_right=(1,1))
        self.assertEqual(1, sq.area())

if __name__ == "__main__":
    unittest.main()