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

Example 2: Vehicle, Car, Motorcycle
class Vehicle:
    def start(self):
        print("Starting the engine...")

    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving on four wheels 🚗")

class Motorcycle(Vehicle):
    def move(self):
        print("The motorcycle is zooming on two wheels 🏍️")

car = Car()
bike = Motorcycle()
car.start()
car.move()
bike.start()
bike.move()


