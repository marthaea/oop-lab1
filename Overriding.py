# Child class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area() method
    def area(self):
        return math.pi * self.radius ** 2


# Child class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Overriding the area() method
    def area(self):
        return self.length * self.width
# Create instances
circle = Circle(7)
rectangle = Rectangle(10, 5)

# Call the overridden methods
print("Circle area:", circle.area())         # Uses Circle’s version
print("Rectangle area:", rectangle.area())   # Uses Rectangle’s version

