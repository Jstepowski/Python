class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return (self.length * 2) + (self.width * 2)

    def display_rectangle():
        pass

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        

rectangle1 = Rectangle(2, 4)

print (rectangle1.length, rectangle1.width, rectangle1.calc_area(), rectangle1.calc_perimeter())
    



