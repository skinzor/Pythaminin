class Circle(object):
    # Class Object Attributes
    pi = 3.141592653589793238  # 18 decimal places (upto)

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        # radius**2 * pi
        return (self.radius ** 2) * Circle.pi


c = Circle(radius=26)
print(c.radius)
print(c.area())
