#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 4, 2021
# This programs asks the user for two numbers and then performs the operation
# the user inputted on those numbers, displaying the result

def calculate(number1, number2, operation):
    # does the operation depending on which one the user inputted
    # displays error message as fail safe
    result = 0
    if (operation == '+'):
        result = number1 + number2
    elif (operation == '-'):
        result = number1 - number2
    elif (operation == '*'):
        result = number1 * number2
    elif (operation == '/'):
        result = number1 / number2
    elif (operation == '%'):
        result = number1 % number2
    else:
        print("{} is not an operation, try again.". format(operation))
    return result


def main():
    # greet message
    print("This program performs calculations between two numbers.")
    print()

    while True:
        # get the operation from the user
        user_oper = input("Enter the operation you want to perform\
 (+, -, *, /, %): ")

        if ((user_oper == '+') or (user_oper == '-') or
                (user_oper == '*') or (user_oper == '/') or
                (user_oper == '%')):
            # check if the user inputted the right operation
            print()
            while True:
                # get the first number from the user
                user_num1_string = input("Enter the first number: ")
                try:
                    # convert from string to float
                    user_num1_float = float(user_num1_string)
                    break
                except ValueError:
                    # error message of the input is not a number
                    print("{} is not a number, try again.\
". format(user_num1_string))
            print()
            while True:
                # get the second number from the user
                user_num2_string = input("Enter the second number: ")
                try:
                    # convert from string to float
                    user_num2_float = float(user_num2_string)
                    break
                except ValueError:
                    # error message of the input is not a number
                    print("{} is not a number, try again.\
". format(user_num2_string))
            # assign calculate function to calc to get the result
            calc = calculate(user_num1_float, user_num2_float, user_oper)
            print()
            # display the result
            print("{0} {1} {2} = {3}\
". format(user_num1_string, user_oper, user_num2_string, calc))
            break
        else:
            # error message if the operation was invalid
            print("{} is not an operation, try again.". format(user_oper))


if __name__ == "__main__":
    main()
