

'''
In math, each 2d dimensional figure (for this example we work with closed figures) has 
- some name (like an identifier), 
- amount of sides (like a number of edges),
- some points (like a list of vertices - for polygons - or center for curved figures).

First, defining some abstract class Figure, with no implementation of methods area and perimeter, they are to be implemented in subclasses.
Considering that each figure has some points, defining a method to calc the distance between two points, 
'cause such method will be used in every figure subclass.

2d dim. figures can be divided into two main categories: polygons and curved figures (i also remember there's a compex shapes, 
but task didnt have 'em)
Polygons are figures with straight edges, while curved figures, well, are figures with curved edges.
Curved figures (such as circle) have a radius and center, while polygons have a number of sides and vertices.

And, using inheritance, we create some subclasses for these 2 categories. So, for example, in task we have rect and square, they are 
polygons with specific properties - while classic polygon area and perimeter counting works for them, 
there are easier formulas that can be executed.

'''

class Figure:
    def __init__(self, name='Figure', sides: int = None, points: list = None):
        self.name = name
        self.sides = abs(sides)
        self.points = points if points is not None else []

    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

    def distance(self, point1, point2) -> float:
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    
    def __str__(self):
        return f"{self.name} Perimeter {self.perimeter()} Area {self.area()}"
    
class Polygon(Figure):
    def __init__(self, name='Polygon', sides: int = None, points: list = None):
        super().__init__(name, sides, points)

    def area(self) -> float:
        verticles = len(self.points)
        # You need at least 3 points to form a polygon
        if verticles < 3:
            return 0
        
        area = 0
        # Using the shoelace formula to calculate the area of a polygon
        # The formula is: 1/2(x1y2 + x2y3 + ... + xn-1yn + xn*y1 - (y1x2 + y2x3 + ... + yn-1xn + yn*x1))

        for i in range(verticles):
            xi, yi = self.points[i]
            x_next, y_next = self.points[(i + 1) % verticles] # % verticles to not go out of bounds
            area += xi * y_next - yi * x_next
        return round(abs(area) / 2, 3)
    
    def perimeter(self) -> float:
        # In case user didn't provide points or provided less than 2 points, return 0, 'cause perimeter is not defined
        if not self.points or len(self.points) < 2:
            return 0
        perimeter = 0
        for i in range(len(self.points)):
            perimeter += self.distance(self.points[i], self.points[(i + 1) % len(self.points)])
        return round(perimeter, 3)

class Rectangle(Polygon):
    def __init__(self, name='Rectangle', width: float = 1.0, height: float = 1.0, bottom_left: tuple = None, top_right: tuple = None):
        if bottom_left and top_right:
            points = self.rect_points(bottom_left, top_right)
            self.width = round(points[1][0] - points[0][0], 3)
            self.height = round(points[2][1] - points[1][1], 3)
        else:
            points = []
            self.width = abs(width)
            self.height = abs(height)

        super().__init__(name, sides=4, points=points)
    
    def rect_points(self, bottom_left, top_right) -> list[tuple]:
        return [
            bottom_left,
            (top_right[0], bottom_left[1]),
            top_right,
            (bottom_left[0], top_right[1])
        ]
    
    def area(self) -> float:
        return round(self.width * self.height, 3) if self.width and self.height else 0
    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 3) if self.width and self.height else 0  
    
class Square(Rectangle):
    def __init__(self, name='Square', side_length: float = 1.0, top_right: tuple = None):
        super().__init__(name, width=side_length, height=side_length, top_right=top_right)
        self.side_length = abs(side_length)

    def area(self) -> float:
        return self.side_length ** 2

    def perimeter(self) -> float:
        return 4 * self.side_length

class Circle(Figure):
    def __init__(self, name='Circle', radius: float = 1.0, center: tuple = (0, 0)):
        super().__init__(name, sides=None, points=[center])
        self.radius = abs(radius)
        self.center = center

    def area(self) -> float:
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius