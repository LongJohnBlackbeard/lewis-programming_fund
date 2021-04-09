# Daniel Tujo]
# Programming Fundamentals
# April 5th 2021

# MUST BE RUN WITH jungle_items.txt IN THE SAME DIRECTORY

import csv

# creates empty lists to hold items, item prices, and for shopping cart
item_list = []
price_list = []
cart = []

# this portion opens the txt file using csv for easier management
# grabs each row and splits using tab as delimiter then saves to a list
# Then adds index 1 to item list and index 2 to price list
with open('jungle_items.txt', "r") as f:
    reader = csv.reader(f)
    for row in reader:
        row_list = row[0].split("\t")
        item_list.append(row_list[1])
        price_list.append(row_list[2])


# Simple and elegant heading
def intro():
    print("-" * 100)
    print("{:^100}".format("The Jungle v106"))
    print("{:^100}".format("We have just about everything!"))
    print("{:^100}".format("Well, not really...."))
    print("-" * 100)


# Prints out all items in the item list with their price from price list
# takes a validated user input, subtracts 1 to match indexes, and adds it to cart list
def print_items_and_get_choice():
    print("What would you like to purchase?")
    for i in range(0, len(item_list)):
        print("%d. %s ($%s)" % (i + 1, item_list[i], price_list[i]))

    item_choice = (int(input("Enter number of choice: ")) - 1)
    while item_choice not in range(0, len(item_list)):
        item_choice = (int(input("Enter number of choice: ")) - 1)
    print("")

    cart.append(item_choice)
    print("%s has been added to your cart." % item_list[item_choice])
    print("")


# If nothing is in cart list, prints appropriate response
# Because cart is filled with numbers that correspond to an index in price and item list this function
# does the following:
# For every number in the cart, uses that number as an index for item lists and prices list and
# prints out every item and price
def show_cart():
    if not cart:
        print("Your cart is empty!")
    else:
        print("Here are the items in your cart:")
        for i in cart:
            print("\t %-15s %10s%6s" % (item_list[i], "$", price_list[i]))
    print("")


# This function Does the similar print out of cart from show cart except printing out the price
# Then in a while loop, asks user for either the number of item to remove, a to clear or blank to cancel
# Using a serious of if and try/catch statements, it validates and checks user input on what to do
# I used a try/catch statement here because the user can either enter a int or a str and want to avoid type errors.
# User input is entered as a string, however if user enters a number it needs to be used as a index for what item in
# the cart to be removed.
# If input is blank, while loop is broken
# if input is "a", confirms user with y/n, if y then cart is emptied and loop is broken, if n then loop is broken
# If input is a valid number, item is removed and loop is broken
# If input does not match any of the above, it loops to the beginning asking user input again
def remove_from_cart():
    print("Here are the items in your cart:")

    for i in range(0, len(cart)):
        print("%i. %s" % (i + 1, item_list[cart[i]]))

    condition = True
    while condition:
        remove_choice = input("Enter the number of the item to remove, 'a' to clear all items, or press Enter to "
                              "cancel: ")
        if remove_choice == "a":
            empty = input("Are you sure you want to empty your cart? (y/n)")
            if empty.lower() == "y":
                cart.clear()
                print("Your cart has been emptied.")
                break
            else:
                break
        elif remove_choice == "":
            break
        try:
            if (int(remove_choice) - 1) in range(0, len(cart)):
                print("")
                print("%s has been removed from your cart!" % (item_list[cart[int(remove_choice) - 1]]))
                cart.pop(int(remove_choice) - 1)
                break
        except TypeError:
            continue
    print("")


# Uses cart list that is full of numbers that correlate to index of price and items lists
# Elegantly prints list of items and prices showing total at the botumn.
def pay_and_close():
    print("Here is what you purchased:")
    total = 0
    for i in cart:
        print("   %-15s %13s%6.2f |" % (item_list[i], "$", float(price_list[i])))
        total += float(price_list[i])
    print("-" * 40)
    print("%-11s %20s%6.2f" % ("Total Cost", "$", total))
    print("")
    print("Thank you for shopping at The Jungle!")


# Uses condition for while loop
# Prints Menu
# asks and validates user input
# each valid input correlates to a function
# if input is 4 (Pay and Exit) loop is broken, end of program
def print_menu_and_get_choice():
    condition = True

    while condition:
        print("What would you like to do?")
        print("1. Shop")
        print("2. See Cart")
        print("3. Remove Items")
        print("4. Pay and Exit")
        choice = int(input("Enter the number of your choice: "))
        while choice not in [1, 2, 3, 4]:
            choice = int(input("Enter the number of your choice(1-4):"))
        print("")

        if choice == 1:
            print_items_and_get_choice()
        elif choice == 2:
            show_cart()
        elif choice == 3:
            remove_from_cart()
        else:
            pay_and_close()
            condition = False
    print("")


# Execution
intro()
print_menu_and_get_choice()
