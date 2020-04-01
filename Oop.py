class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius)  * (self.radius)
        print(area)

Circle1 = Circle(5)
Circle2 = Circle(6)

Circle1.area()
Circle2.area()