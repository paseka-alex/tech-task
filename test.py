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

class TestRectangle(unittest.TestCase):
    def SetUp():
        pass

    def test_perimeter1(self):
        rect = figures.Rectangle(bottom_left=(1,1), top_right=(2,4))
        self.assertEqual(8, rect.perimeter())

    def test_area1(self):
        rect = figures.Rectangle(bottom_left=(1,1), top_right=(2,4))
        self.assertEqual(3, rect.area())

    def test_points(self):
        rect = figures.Rectangle(bottom_left=(1,1), top_right=(2,4))
        self.assertEqual([(1, 1), (2, 1), (2, 4), (1, 4)], rect.points)

    def test_perimeter1_sides(self):
        rect = figures.Rectangle(width=2, height=3)
        self.assertEqual(10.0, rect.perimeter())

    def test_area1_sides(self):
        rect = figures.Rectangle(width=2, height=3)
        self.assertEqual(6.0, rect.area())

class TestPolygon(unittest.TestCase):
    def SetUp():
        pass

    def test_perimeter1(self):
        polyg = figures.Polygon(sides=4, points=[(1, 1), (2, 1), (2, 4), (1, 4)])
        self.assertEqual(8, polyg.perimeter())
if __name__ == "__main__":
    unittest.main()