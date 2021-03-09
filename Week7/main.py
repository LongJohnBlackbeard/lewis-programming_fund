# Daniel Tujo
# Programming Fundamentals
# Week 7

class Triangle:
    def __init__(self, base=0, height=0, side1=0, side2=0, side3=0, area=0, triangle_type="Triangle"):
        self._area = area
        self._base = base
        self._height = height
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._triangle_type = triangle_type

    def set_base_height(self):
        self._base = int(input("Enter base: "))
        while self._base <= 0:
            self._base = int(input("Enter base(greater than 0): "))

        self._height = int(input("Enter height: "))
        while self._height <= 0:
            self._height = int(input("Enter height(greater than 0): "))

    def get_base_height(self):
        return self._base, self._height

    def find_area(self):
        self._area = 0.5 * self._base * self._height
        return self._area

    def set_sides(self):
        while self._side1 <= 0:
            self._side1 = int(input("Enter side 1: "))
        while self._side2 <= 0:
            self._side2 = int(input("Enter side 2: "))
        while self._side3 <= 0:
            self._side3 = int(input("Enter side 3: "))

    def get_sides(self):
        return self._side1, self._side2, self._side3

    def find_type(self):
        if self._side1 == self._side2 and self._side1 != self._side3:
            self._triangle_type = "Isosceles"
        elif self._side1 == self._side3 and self._side1 != self._side2:
            self._side1 = "Isosceles"
        elif self._side2 == self._side3 and self._side2 != self._side1:
            self._triangle_type = "Isosceles"
        elif self._side1 == self._side2 == self._side3:
            self._triangle_type = "Equilateral"
        else:
            self._triangle_type = "Scalene"
        return self._triangle_type

    def output(self):
        print("This %s triangle has area %.2f." % (self._triangle_type, self._area))


continue_condition = True
while continue_condition:
    tri = Triangle()
    tri.set_base_height()
    tri.set_sides()
    tri.find_area()
    tri.find_type()
    tri.output()

    cont = input("Would you like to continue yes(y) or no(n): ")
    while (cont.lower() != "y") and (cont.lower() != "n"):
        cont = input("Would you like to continue yes(y) or no(n): ")
    if cont == "y":
        continue_condition = True
    else:
        continue_condition = False





