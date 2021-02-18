# Daniel Tujo
# Programming Fundamentals
# February 17th, 2021


# Requirements:
# Nicely Formatted and centered heading

# Ask user for the degree of the polynomial and then for the correct, relevant coefficients, and min/max x values
# Print "Here is f(x)=" followed by the coefficient of the correct degree and coefficients and the domain expressed
# as [xmin,xmax]
# Calculate the value of f(x) over the specified domain correctly
# Represent result nicely in a table with boundaries and with the headings  "x" and "f(x) centered atop each column
# Ask user if they want to enter another polynomials, and repeat process, end if not.
# Sprinkle helpful comments
# Submit program to blackboard "lastname_polynomial.py"


def getConstant():
    constant = inputFloatNumber("Enter the constant: ")
    return constant


def getStartValues():
    startValue = inputIntNumber("Enter the starting value of x: ")
    return startValue


def getEndValues():
    endValue = inputIntNumber("Enter the ending value of x: ")
    return endValue


def inputIntNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please enter a whole number! ")
            continue
        else:
            return userInput
        break


def inputFloatNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Please enter a whole number! ")
            continue
        else:
            return userInput
        break


def intro():
    print("*" * 70)
    print("*%s*" % "POLYNOMIAL PLOTTER".center(68))
    print("*" * 70)
    print("")


def outro():
    print("")
    print("Thank you for using this program.")


def tryAgain():
    again = input("Do you want to try another (y or n)? ")
    while again.lower() not in ["y", "n"]:
        again = input("Do you want to try another (y or n)? ")
    if again.lower() == "y":
        return True
    else:
        return False


class MyPolynomial:

    def __init__(self):

        self.coefficientList = []
        self.degree = int(input("Enter the degree of the polynomial (1, 2, 3, or 4): "))
        while self.degree not in [1, 2, 3, 4]:
            self.degree = int(input("Please enter a valid number (1, 2, 3, or 4) : "))

        self.coefficients = 0
        self.constant = 0
        self.startValue = 0
        self.endValue = 0
        self.yValueList = []

    def getCoefficients(self):

        self.coefficientList.clear()

        if self.degree == 4:
            self.coefficientList.append(float(input("Enter the coefficient of the x^4 term: ")))
            self.coefficientList.append(float(input("Enter the coefficient of the x^3 term: ")))
            self.coefficientList.append(float(input("Enter the coefficient of the x^2 term: ")))
            self.coefficientList.append(float(input("Enter the coefficient of the x term: ")))
        elif self.degree == 3:
            self.coefficientList.append(0)
            self.coefficientList.append(float(input("Enter the coefficient of the x^3 term: ")))
            self.coefficientList.append(float(input("Enter the coefficient of the x^2 term: ")))
            self.coefficientList.append(float(input("Enter the coefficient of the x term: ")))
        elif self.degree == 2:
            self.coefficientList.append(0)
            self.coefficientList.append(0)
            self.coefficientList.append(float(input("Enter the coefficient of the x^2 term: ")))
            self.coefficientList.append(float(input("Enter the coefficient of the x term: ")))
        else:
            self.coefficientList.append(0)
            self.coefficientList.append(0)
            self.coefficientList.append(0)
            self.coefficientList.append(float(input("Enter the coefficient of the x term: ")))

        return self.coefficientList

    def calculateYValue(self):
        self.coefficients = self.getCoefficients()
        self.constant = getConstant()
        self.startValue = getStartValues()
        self.endValue = getEndValues()

        for i in range(self.startValue, self.endValue + 1):
            if len(self.coefficients) in [1, 2, 3, 4]:
                firstCoefficient = (self.coefficients[0] * (i * i * i * i))
                secondCoefficient = (self.coefficients[1] * (i * i * i))
                thirdCoefficient = (self.coefficients[2] * (i * i))
                fourthCoefficient = (self.coefficients[3] * i)
                y = (firstCoefficient + secondCoefficient + thirdCoefficient + fourthCoefficient + self.constant)
                self.yValueList.append(y)
            else:
                pass

    def showPolynomial(self):
        print("")
        if self.degree == 4:
            print("Here is f(x) = %.2fx^4 + %.2fx^3 + %.2fx^2 + %.2fx + %.2f over domain [%d,%d]:" %
                  (self.coefficients[0], self.coefficients[1], self.coefficients[2], self.coefficients[3],
                   self.constant, self.startValue, self.endValue))
        elif self.degree == 3:
            print("Here is f(x) = %.2fx^3 + %.2fx^2 + %.2fx + %.2f over domain [%d,%d]:" %
                  (self.coefficients[1], self.coefficients[2], self.coefficients[3],
                   self.constant, self.startValue, self.endValue))
        elif self.degree == 2:
            print("Here is f(x) = %.2fx^2 + %.2fx + %.2f over domain [%d,%d]:" %
                  (self.coefficients[2], self.coefficients[3], self.constant, self.startValue, self.endValue))
        else:
            print("Here is f(x) = %.2fx + %.2fx over domain [%d,%d]:" %
                  (self.coefficients[3], self.constant, self.startValue, self.endValue))

    def showTable(self):

        print("*", "-" * 17, "*")
        print("|%s|%s|" % ("x".center(9), "y".center(9)))
        print("|", "-" * 17, "|")
        yValuePosition = 0
        for i in range(self.startValue, self.endValue + 1):
            print("|%9.2f|%9.2f|" % (i, self.yValueList[yValuePosition]))
            yValuePosition += 1
        print("*", "-" * 17, "*")
        print("")


def output():
    intro()
    condition = True
    while condition:
        obj = MyPolynomial()
        obj.calculateYValue()
        obj.showPolynomial()
        obj.showTable()
        condition = tryAgain()
    else:
        pass
    outro()


output()
