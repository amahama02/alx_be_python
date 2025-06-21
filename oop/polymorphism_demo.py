import math

class Shape:
    """
    Base class for all shapes.
    Defines a common interface for calculating area, which must be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by any concrete subclass.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance with given length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    """
    def __init__(self, radius: float):
        """
        Initializes a Circle instance with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of the circle.
        Formula: π * radius^2
        """
        return math.pi * (self.radius ** 2)