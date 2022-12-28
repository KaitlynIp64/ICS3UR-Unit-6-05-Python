#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program calculates the average mark


def find_the_average_mark(marks):
    # This function finds the average

    total = 0

    for element in marks:
        total += element
    average = total / len(marks)
    return average


def main():
    # This function makes the list

    marks = []
    temp_int = None

    # Input
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    while True:
        try:
            temp_num = input("What is your mark? (as %): ")
            temp_int = int(temp_num)
            if temp_int <= 100 and temp_int >= 0:
                marks.append(temp_int)
            elif temp_int == -1:
                average = find_the_average_mark(marks)
                print("\nYour average is: {0}%".format(average))
                break
            temp_int = int(temp_num)
            marks.append(temp_int)
        except ValueError:
            print("That is not a valid input. Try again.")
            continue

    print("\nDone.")


if __name__ == "__main__":
    main()
