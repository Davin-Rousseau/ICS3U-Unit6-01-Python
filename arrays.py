#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: December 2019
# This program uses an array and prints out 10
# numbers from 1-100 and takes average of them

import random


def main():
    # this function uses an array and calculates average
    # of 10 random numbers

    random_list = []
    total_number = 0

    for counter in range(0, 9+1):
        random_number = random.randint(0, 100+1)
        random_list.append(random_number)
    print("")

    print("Here are the 10 numbers:")

    for counter in range(0, 9+1):
        print("{0}, ".format(random_list[counter]), end="")

    print("")
    print("The average of the 10 numbers is: ")

    for counter in range(0, 9+1):
        total_number = random_list[counter] + total_number

    total_number = total_number / 10
    print("{0}".format(total_number))


if __name__ == "__main__":
    main()
