# Daniel Tujo
# Programming Fundamentals
# February 17th, 2021
# Polynomial Plotter
# Purpose: Calculate a polynomial over a domain range, giving the user an option of 1, 2, 3, or 4 degree polynomial.
# Than presenting data results in a table.


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


def getConstant():  # function for grabbing a constant used later
    constant = inputFloatNumber("Enter the constant: ")
    return constant


def getStartValues():  # function for grabbing domain start value used later
    startValue = inputIntNumber("Enter the starting value of x: ")
    return startValue


def getEndValues():  # function for grabbing domain end value used later
    endValue = inputIntNumber("Enter the ending value of x: ")
    return endValue


def inputIntNumber(message):  # function validating user input is an integer, used in get methods
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please enter a whole number! ")
            continue
        else:
            return userInput
        break


def inputFloatNumber(message):  # function validating user input is a float, used in get methods
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Please enter a valid number! ")
            continue
        else:
            return userInput
        break


def intro():  # function that prints out Heading
    print("*" * 70)
    print("*%s*" % "POLYNOMIAL PLOTTER".center(68))
    print("*" * 70)
    print("")


def outro():  # function that prints ou ending message
    print("")
    print("Thank you for using this program.")


def tryAgain():  # function that asks if user wants try again, validates input, and returns a boolean
    again = input("Do you want to try another (y or n)? ")
    while again.lower() not in ["y", "n"]:
        again = input("Do you want to try another (y or n)? ")
    if again.lower() == "y":
        return True
    else:
        return False


class MyPolynomial:  # Trying to incorporate classes into my work now
    # Main class the performs all the calculations, and print statements

    def __init__(self):  # default constructor, and sets default values

        self.coefficientList = []
        self.degree = int(input("Enter the degree of the polynomial (1, 2, 3, or 4): "))
        while self.degree not in [1, 2, 3, 4]:
            self.degree = int(input("Please enter a valid number (1, 2, 3, or 4) : "))

        self.coefficients = 0
        self.constant = 0
        self.startValue = 0
        self.endValue = 0
        self.yValueList = []

    def getCoefficients(self):  # method that grabs the coefficient value and appends it to a list.
        # For a list to work here, you still need to pass a value in for 4 different coefficients, however,
        # if a degree is smaller than 4, it will just add 0 to the list for the correlating coefficients. Returns
        # the list

        if self.degree == 4:
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x^4 term: "))
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x^3 term: "))
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x^2 term: "))
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x term: "))
        elif self.degree == 3:
            self.coefficientList.append(0)
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x^3 term: "))
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x^2 term: "))
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x term: "))
        elif self.degree == 2:
            self.coefficientList.append(0)
            self.coefficientList.append(0)
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x^2 term: "))
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x term: "))
        else:
            self.coefficientList.append(0)
            self.coefficientList.append(0)
            self.coefficientList.append(0)
            self.coefficientList.append(inputFloatNumber("Enter the coefficient of the x term: "))

        return self.coefficientList

    def calculateYValue(self):  # Method that calculates the sum (y value). This method also executes the
        # previous method that grabs the Coefficients in a list
        self.coefficients = self.getCoefficients()
        self.constant = getConstant()
        self.startValue = getStartValues()
        self.endValue = getEndValues()

        for i in range(self.startValue, self.endValue + 1):  # for loop for the value given for the domain range
            # the for loop does the following calculations for every x value in the domain range
            firstCoefficient = (self.coefficients[0] * (i * i * i * i))
            secondCoefficient = (self.coefficients[1] * (i * i * i))
            thirdCoefficient = (self.coefficients[2] * (i * i))
            fourthCoefficient = (self.coefficients[3] * i)
            y = (firstCoefficient + secondCoefficient + thirdCoefficient + fourthCoefficient + self.constant)
            self.yValueList.append(y)  # appends the y value to a list

    def showPolynomial(self):  # method that user if statement to determine what degree polynomial to print
        print("")  # print statement is formatted in correlation with what degree the polynomial is
        if self.degree == 4:  # Uses class variables, and to pass in values
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

    def showTable(self):  # Method the prints out the table containing x and y values of the polynomial

        print("*", "-" * 17, "*")
        print("|%s|%s|" % ("x".center(9), "y".center(9)))
        print("|", "-" * 17, "|")
        yValuePosition = 0
        for i in range(self.startValue, self.endValue + 1):
            print("|%9.2f|%9.2f|" % (i, self.yValueList[yValuePosition]))
            yValuePosition += 1
        print("*", "-" * 17, "*")
        print("")


def output():  # this  is the execution function
    intro()  # executes header method
    condition = True  # set a condition for a while loop
    while condition:  # while loop used in correlation with tryagain method to determine if the user want to try again
        obj = MyPolynomial()  # creates an obj of the polynomial class
        obj.calculateYValue()  # executes methods from polynomial class
        obj.showPolynomial()  # executes methods from polynomial class
        obj.showTable()  # executes methods from polynomial class
        condition = tryAgain()  # sets the condition from the tryagain function. tryagain will return true if
        # the user wants to do another one, of false if the user doesnt. False will break the while loop
    else:
        pass
    outro()     # executes the ending message function


output() #this executes the whole program
