#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program checks if there is over 30 students


import constants


def main():
    # this function checks if there is over 30 students

    # input
    number = int(input("Enter the number I guessed: "))
    print("")

    # process & output
    if number == constants.NUMBER_I_CHOOSE:
        print("You guessed it!")
    else:
        print("You couldn't guess it")


if __name__ == "__main__":
    main()
