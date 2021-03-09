# Daniel Tujo
# Programming Fundamentals
# Football Turtle
import turtle
import random

# Set initial window and turtle
window = turtle.Screen()
window.setup(1200, 800, 0, 0)
window.bgcolor("Green")
turt = turtle.Turtle()
turt.hideturtle()


# validates user input for run/pass prompt
def runPassValidate():
    pass_or_run = input("Would you like to run (r) or pass (p) the ball? ")
    while pass_or_run.lower() not in ["r", "p"]:
        pass_or_run = input("Enter Valid letter (Run = r and Pass = p): ")
    return pass_or_run


# random number generate for a run call
def run():
    yards = random.randint(-3, 8)
    return yards


# function for a pass play, random 50/50 for completion, and random yards between 3-15
def passPlay():
    success_failure = random.randint(1, 2)
    if success_failure == 1:
        yards = 0
    else:
        yards = random.randint(3, 15)

    return yards


# function that prints result of a run play to the terminal
def runResult(yards):
    if yards > 0:
        print("Run for a gain of %d yards." % yards)
    elif yards == 0:
        print("Run for no gain")
    else:
        print("Run for a loss of %d yards." % yards)


# function that prints result of pass play to terminal
def passResult(yards):
    if yards == 0:
        print("Incomplete Pass")
    else:
        print("Pass Complete for a gain of %d yards." % yards)


# core component to game
def game():
    # uses turt to draw blank score area in case of multiple games being played
    freshScoreBoard()
    # draw initial down and yardage on scoreboard
    turt.penup()
    turt.goto(0, -350)
    turt.pencolor(.96, .6, .18)
    turt.pendown()
    turt.write("1st and 10 on the 25", False, align="left", font=("Arial", 20, "normal"))

    # creates new turtle that act just as the football
    football = turtle.Turtle()
    football.shape("turtle")
    football.color(.51, .32, .1)
    football.penup()

    # initial values to be used in loops and if statements
    yard_counter = 0
    down_counter = 1
    yard_till_first = 10
    football.goto(-375, 0)
    last_football_xPos = -375
    yardLine = 25

    # loop checks to see if out of downs or have enough yards for a touchdown
    while yard_counter <= 30 and down_counter < 5 and yardLine > 0:
        # call validate function
        pass_or_run = runPassValidate()
        # if statement for run play, calls random generated run yards, tallies yards to yard counter, prints results
        # set position using yard constant of 25, adds yard counter, down counter, and yards till first down counter
        if pass_or_run == "r":
            yards = run()
            yardLine -= yards
            runResult(yards)
            last_football_xPos += (yards * 25)
            yard_counter += yards
            down_counter += 1
            yard_till_first -= yards
            # if statement for 1st downs, if first down, resets counters
            if yard_till_first <= 0:
                yard_till_first = 10
                down_counter = 1
            # sends turtle to where next play should be
            football.goto(last_football_xPos, 0)
            # updates scoreboard using function
            updateScoreBoard(down_counter, yard_till_first, yardLine)
        # same thing as run play
        if pass_or_run == "p":
            yards = passPlay()
            yardLine -= yards
            passResult(yards)
            last_football_xPos += (yards * 25)
            yard_counter += yards
            down_counter += 1
            yard_till_first -= yards
            if yard_till_first <= 0:
                yard_till_first = 10
                down_counter = 1
            football.goto(last_football_xPos, 0)
            updateScoreBoard(down_counter, yard_till_first, yardLine)
    # if you you get to yardline 0 or less print this to terminal
    if yardLine <= 0:
        print("Touchdown!! Game Over!! You Win!")
        scoreChange()
    # if you run out of downs, prints this to terminal
    if down_counter == 5:
        print("Turn over on downs! Game Over! You Lost!")
    # hides turtle incase multiple games you wont have multiple turtles on screen
    football.hideturtle()


# turtle that draws the field
def drawField():
    footballField = turtle.Turtle()
    footballField.speed(0)
    footballField.penup()
    footballField.goto(-600, 250)

    footballField.pencolor(.75, .75, .75)
    footballField.pensize(5)
    footballField.pendown()

    footballField.goto(500, 250)
    footballField.goto(500, -250)
    footballField.goto(-600, -250)
    footballField.goto(-500, -250)
    footballField.goto(-500, 250)
    footballField.goto(-375, 250)
    footballField.goto(-375, -250)
    footballField.goto(-250, -250)
    footballField.goto(-250, 250)
    footballField.goto(-125, 250)
    footballField.goto(-125, -250)
    footballField.goto(0, -250)
    footballField.goto(0, 250)
    footballField.goto(125, 250)
    footballField.goto(125, -250)
    footballField.goto(250, -250)
    footballField.goto(250, 250)
    footballField.penup()

    footballField.goto(495, 245)
    footballField.fillcolor(0, 0, 1)
    footballField.begin_fill()
    footballField.pencolor(0, 0, 1)
    footballField.pendown()
    footballField.goto(495, -245)
    footballField.goto(255, -245)
    footballField.goto(255, 245)
    footballField.goto(495, 245)
    footballField.end_fill()
    footballField.penup()
    footballField.pencolor(.75, .75, .75)

    xStart = -525
    value = 4
    # couple for loops to help automate number drawing
    for i in range(0, 3):
        value -= 1
        drawNumber(value, footballField, xStart, 200)
        xStart += 250

    xStart = -495
    for i in range(0, 3):
        drawNumber(0, footballField, xStart, 200)
        xStart += 250

    xStart = -525
    value = 4
    for i in range(0, 3):
        value -= 1
        drawNumber(value, footballField, xStart, -250)
        xStart += 250

    xStart = -495
    for i in range(0, 3):
        drawNumber(0, footballField, xStart, -250)
        xStart += 250

    # call hash mark function (draws hash marks)
    hashMarks(footballField, -500, 25, 50)
    hashMarks(footballField, -500, 25, -50)

    # calls scoreboard function (draws initial scoreboard)
    scoreboard(footballField)


# function that draws a black square over down and yardage for new games
def freshScoreBoard():
    turt.penup()
    turt.pencolor(0, 0, 0)
    turt.goto(0, -350)
    turt.pendown()
    turt.fillcolor(0, 0, 0)
    turt.begin_fill()
    turt.goto(0, -400)
    turt.goto(300, -400)
    turt.goto(300, -300)
    turt.goto(0, -300)
    turt.goto(0, -400)
    turt.end_fill()
    turt.penup()


# function that runs after every play to update down and yardage on scoreboard
def updateScoreBoard(down, yards, yardline):
    turt.pencolor(0, 0, 0)
    turt.penup()
    turt.goto(0, -350)
    turt.pendown()
    turt.fillcolor(0, 0, 0)
    turt.begin_fill()
    turt.goto(0, -400)
    turt.goto(300, -400)
    turt.goto(300, -300)
    turt.goto(0, -300)
    turt.goto(0, -400)
    turt.end_fill()
    turt.penup()

    turt.pencolor(.96, .6, .18)
    turt.pensize(5)
    turt.hideturtle()
    turt.penup()
    turt.goto(0, -350)
    turt.pendown()
    # series of if statements, calculates what to draw based on down and yardage as well as if your yardage should be
    # x and "goal". Also prints game over for turnover on downs, and touchdowns.
    if down < 5 and yardline > 0:
        if down == 1:
            down = "1st"
        elif down == 2:
            down = "2nd"
        elif down == 3:
            down = "3rd"
        else:
            down = "4th"
        if yardline < 10 and yards <= 10 and down == "1st":
            yards = "Goal"
        turt.write("%s and %s on the %d" % (down, str(yards), yardline), False, align="left",
                   font=("Arial", 20, "normal"))
    elif down > 4:
        turt.write("Turnover On Downs", False, align="left", font=("Arial", 20, "normal"))
    else:
        turt.write("Touchdown! Game Over!", False, align="left", font=("Arial", 20, "normal"))


# function that changes value on scoreboard if there is a touchdown
def scoreChange():
    turt.penup()
    turt.pencolor(0, 0, 0)
    turt.fillcolor(0, 0, 0)
    turt.begin_fill()
    turt.goto(-125, -340)
    turt.pendown()
    turt.goto(-50, -340)
    turt.goto(-50, -300)
    turt.goto(-125, -300)
    turt.goto(-125, -340)
    turt.end_fill()
    turt.penup()
    turt.pencolor(.96, .6, .18)
    turt.goto(-270, -340)
    turt.pendown()
    turt.write("%20d" % 6, False, align="left", font=("Arial", 20, "normal"))


# function that draws initial scoreboard
def scoreboard(turt):
    turt.penup()
    turt.fillcolor(0, 0, 0)
    turt.pencolor(0, 0, 0)
    turt.goto(300, -400)
    turt.begin_fill()
    turt.pendown()
    turt.goto(300, -300)
    turt.goto(-300, -300)
    turt.goto(-300, -400)
    turt.goto(300, -400)
    turt.penup()
    turt.end_fill()

    team_name = "Klumpsters"
    turt.goto(-270, -340)
    turt.pencolor(.96, .6, .18)
    turt.write("%-10s" % (team_name.title()), False, align="left", font=("Arial", 20, "normal"))
    turt.write("%20d" % 0, False, align="left", font=("Arial", 20, "normal"))
    turt.goto(-270, -370)
    turt.write("%-10s" % "Kujos", False, align="left", font=("Arial", 20, "normal"))
    turt.write("%20d" % 3, False, align="left", font=("Arial", 20, "normal"))
    turt.hideturtle()


# function that draws hash marks in increments of 1 yard
def hashMarks(ball_turtle, x_start, increment, y):
    ball_turtle.penup()
    ball_turtle.goto(x_start, y)
    for i in range(0, 30):
        ball_turtle.goto(x_start, y)
        ball_turtle.pendown()
        ball_turtle.goto(x_start, y - 5)
        ball_turtle.penup()
        x_start += increment


# function used to draw numbers on the field
def drawNumber(value, field_turtle, x, y):
    field_turtle.penup()
    field_turtle.goto(x, y)
    field_turtle.pendown()
    field_turtle.write(str(value), False, align="left", font=("Clarendon", 30, "normal"))


# execution area
drawField()
# uses while loop to ask users for multiple games
again = True
while again:
    game()
    playAgain = input("Would you like to play again? Yes(y) or No(n): ")
    while playAgain.lower() not in ["y", "n"]:
        playAgain = input("Invalid Answer. Enter y for Yes and n for No: ")
    if playAgain == "y":
        again = True
    else:
        again = False
        turtle.bye()
