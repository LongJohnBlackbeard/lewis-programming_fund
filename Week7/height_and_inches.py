# Daniel Tujo
# Programming Fundamentals
# height in inches

class Height:

    def __init__(self, inches=0, feet=0, cm=0, remaining_inches=0):
        self._inches = inches
        self._remaining_inches = remaining_inches
        self._feet = feet
        self._cm = cm

    def set_inches(self):
        self._inches = int(input("Enter height in inches: "))
        while self._inches <= 0:
            self._inches = int(input("Enter height in inches: "))

    def get_inches(self):
        return self._inches

    def feet_and_inches(self):
        self._feet = self._inches / 12
        self._remaining_inches = self._inches % 12

    def metric(self):
        self._cm = self._inches * 2.54

    def output(self):
        print("You are %d feet, %d inches, or %.2f cm, tall" % (self._feet, self._remaining_inches, self._cm))


p1 = Height()
p1.set_inches()
p1.feet_and_inches()
p1.metric()
p1.output()


