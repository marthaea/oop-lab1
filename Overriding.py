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

# Example 3: Employee, Manager, Developer
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Oversees projects and teams."

class Developer(Employee):
    def get_details(self):
        return f"Developer: {self.name}, Salary: {self.salary}, Writes and tests code."

manager = Manager("Alice", 90000)
developer = Developer("Bob", 70000)
print(manager.get_details())
print(developer.get_details())



# Example 4: Instrument, Guitar, Piano
class Instrument:
    def play(self):
        print("Playing an instrument... 🎵")

class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar strings 🎸")

class Piano(Instrument):
    def play(self):
        print("Pressing the piano keys 🎹")

guitar = Guitar()
piano = Piano()
guitar.play()
piano.play()


# Example 5: Drink, Tea, Coffee
class Drink:
    def prepare(self):
        print("Preparing a drink... ☕")

class Tea(Drink):
    def prepare(self):
        print("Boiling water, steeping tea leaves 🍵")

class Coffee(Drink):
    def prepare(self):
        print("Brewing coffee grounds ☕")

tea = Tea()
coffee = Coffee()
tea.prepare()
coffee.prepare()


# Example 6: Notification, EmailNotification, SMSNotification
class Notification:
    def send(self, message):
        print(f"Sending message: {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

email_notifier = EmailNotification()
sms_notifier = SMSNotification()
email_notifier.send("Welcome to the system!")
sms_notifier.send("Your verification code is 1234.")


