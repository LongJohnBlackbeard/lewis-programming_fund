# Daniel Tujo
# Programming Fundamentals
# question three
import math


class Line:
    def __init__(self, slope=0, distance=0, yint=0, first_p_x=0, first_p_y=0, second_p_x=0, second_p_y=0):
        self._slope = slope
        self._distance = distance
        self._yint = yint
        self._first_p_x = first_p_x
        self._first_p_y = first_p_y
        self._second_p_x = second_p_x
        self._second_p_y = second_p_y

    def set_points(self):
        self._first_p_x = float(input("Enter the x coordinate of the first point: "))
        self._first_p_y = float(input("Enter the y coordinate of the first point: "))
        self._second_p_x = float(input("Enter the x coordinate of the second point: "))
        self._second_p_y = float(input("Enter the y coordinate of the second point: "))

    def find_slope(self):
        self._slope = (self._second_p_y - self._first_p_y) / (self._second_p_x - self._first_p_x)

    def find_dist(self):
        self._distance = math.sqrt(
            ((self._second_p_x - self._first_p_x) ** 2) + ((self._second_p_y - self._first_p_y) ** 2))

    def find_yint(self):
        self._yint = self._first_p_y - (self._slope * self._first_p_x)

    def output(self):
        print("The points (%.2f, %.2f) and (%.2f, %.2f) are %.2f apart" % (self._first_p_x, self._first_p_y,
                                                                           self._second_p_x, self._second_p_y,
                                                                           self._distance))
        print("The line joining them has slope %.2f and crosses the y axis at y = %.2f" % (self._slope, self._yint))


newLine = Line()
newLine.set_points()
newLine.find_slope()
newLine.find_dist()
newLine.find_yint()
newLine.output()
