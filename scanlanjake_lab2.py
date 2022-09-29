"""Program that starts the user with options to chose from and select.\
Then the program runs the determined statements and such to get the users desired outcomes./
from their desired choice and ask(at the end) if the user would like to make any more decisions"""

# Imports different datatypes that have different built-in functions
import datetime
import math
import string
import secrets


def secure_pass():
    """Function to build a secure password"""
    # Variable to store the length the customer has chosen
    length = int(input("How long do you need the password to be?\n"))
    # Variable to store what the user would like done their newly created password\
    # and runs specific statements based on input
    complexity = input("Does your app need all lower case, upper case or special characters?"
                       " answer with 'lower' 'upper' or 'special'\n")
    # Creates the line of letters otherwise known as the alphabet
    alphabet = string.ascii_letters + string.digits
    # Start of loop
    while True:
        # Stores each letter into password, randomly chosen until the length stated is reached
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    # If user wants lower case, prints all letters as a lower
    if complexity == "lower":
        # If user wants upper case, prints all letters as upper
        print(password.lower())
    elif complexity == "upper":
        print(password.upper())
        # Else prints out and runs the statements for special characters
    else:
        space = input("Do you want the special character at the beginning or end?"
                      " Answer with beginning or end\n")
        # If user states beginning, puts the character at the beginning of the password
        if space == "beginning":
            print("!" + password)
        # IF user states end, puts the character at the end of the password
        elif space == "end":
            print(password + "!")


def percent():
    """Function to determine a percentage"""
    # Asks user for a number(numerator) that they want to have be divided
    numerator = float(input("Please enter a numerator(number to be divided by denominator).\n"))
    # Asks user for a number(denominator) to divide the numerator
    denominator = float(input("As well as a denominator.\n"))
    # Variable decimalplace to ask the user how many decimal places they would like to show
    decimalplace = float(input("How many decimal places would you like to show?\n"))
    # Variable percentage to divide the numerator by the denominator
    percentage = numerator / denominator
    # Variable decimal to hold the percentage value
    decimal = percentage

    # Statement to print 1 decimal place if user chooses
    if decimalplace == 1:
        decimal = f'{percentage:.1f}'

    # Statement to print 1 decimal place if user chooses
    elif decimalplace == 2:
        decimal = f'{percentage:.2f}'

    # Statement to print 1 decimal place if user chooses
    elif decimalplace == 3:
        decimal = f'{percentage:.3f}'
    # If user chooses higher than 3 decimal places,\
    # prints following statement. Need to stop them somewhere.
    else:
        print("Error, things are getting a little out of hand.\n")
    print(decimal)


def date_find():
    """Function to print the current date and then\
     find out the amount of days left until July,7,2025"""
    # Variable today, to hold the current days date and print it
    today = datetime.date.today()
    print("Today's date is " + str(today) + ".")

    # Variable future_day, to hold the set date of july,7,2025
    future_day = datetime.date(2025, 0o7, 0o4)
    # Variable days_till subtracts the value of today from future_day\
    # and prints the remaining days until future
    days_till = str(future_day - today)
    print("There are " + days_till + " days until the future date of July,4,2025!\n")


def cosine_triangle():
    """Function to calculate the missing side length of an inputted triangle from user"""
    # Lets user know that we are finding out the missing side C
    print("We're going to find the missing side 'c' of the triangle you describe.\n")
    # Variable a_side to store length of side a
    a_side = float(input("Please give me a length for side a.\n"))
    # Variable b_side to store length of side b
    b_side = float(input("Please give me a length for side b.\n"))

    # Variable all_sides does the calculation to find out the missing side using cosine
    all_sides = (a_side ** 2 + b_side ** 2) - ((2 * a_side * b_side) * math.acos(a_side / b_side))
    # Finds the square root of all_sides
    squared = (math.sqrt(all_sides))
    # Prints all_sides value with 2 decimal places and records it as sice C
    print(f'{squared:.2f}' + " is the size of side c.\n")


def volume_cylinder():
    """Function to find the volume of a right circular cylinder inputted by user"""
    # Let's use know we are calculating the volume of a cylinder
    print("We are going to find the volume of your cylinder.\n")

    # Asks user for the radius
    radius = float(input("Please give me the radius.\n"))
    # Asks user for the height
    height = float(input("Please give me the height.\n"))
    # Variable start_equ to do the first half of the equation to find the volume
    start_equ = (radius ** 2) * height
    # Variable vol to finish the calculation by multiplying start_equ and vol together
    vol = start_equ * 3.14
    # Prints volume
    print(vol)
    print("Is the volume of your cylinder.\n")


def main():
    """Main function to print the main menu
    Gives user choices to do different things"""
    print("[1] Generate a password.\n"
          "[2] Calculate and form a percentage.\n"
          "[3] How many days are there until July 4, 2025?\n"
          "[4] Use cosines to calculate the leg of triangle.\n"
          "[5] Calculate the volume of a right circular cylinder\n"
          "[0] Exit the program.\n")


# calls main() to print menu and then asks user for a choice of something to do
main()
selection = int(input("What would you like to do at this fine moment?\n"))
# Enters while loop, while selection is not 0 the loop will continue
while selection != 0:
    # If 1, calls secure_pass function
    if selection == 1:
        secure_pass()
    # If 2, calls percent function
    elif selection == 2:
        percent()
    # if 3, calls date_find function
    elif selection == 3:
        date_find()
    # if 4, calls cosine_triangle function
    elif selection == 4:
        cosine_triangle()
    # if 5, calls volume_cylinder function
    elif selection == 5:
        volume_cylinder()

    # Calls main() and asks user if they would like to make another selection
    main()
    selection = int(input("Would you like to make another saucy selection?\n"))
    # If 0, exits the program and while loop, and thanks the user for using the program
    if selection == 0:
        print("Thank you for using the program, have a nice day!")
