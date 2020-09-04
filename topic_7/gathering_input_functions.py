"""
Program: gathering_input_functions.py
Author: Daniel Meeker
Date: 9/3/2020

This program will ask a user how many numbers they
want to enter then save their numbers to a list,
output the list, and calculate the average of the list
"""


def how_many_numbers():
    """
    this function is used to prompt the user for input
    to determine how many numbers they want to enter
    :return: int
    """
    flag = False
    while not flag:
        number_of_inputs = input("How many numbers do you want to enter? (Enter x to exit) ")
        if number_of_inputs == 'x' or number_of_inputs == 'X':
            raise ValueError("Program closed by user")
        try:
            number_of_inputs = int(number_of_inputs)
            if number_of_inputs > 0:
                flag = True
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Must be an integer.")
    return number_of_inputs


def numbers_to_store():
    """
    This function is used to prompt the user for the
    integers they want saved in the list
    :return:
    """
    list_length = how_many_numbers()
    number_list = []
    for x in range(list_length):
        flag = False
        while not flag:
            if x == list_length - 1:
                number_to_append = input("Please enter your last number: ")
            else:
                number_to_append = input('Please input a number: ')
            try:
                number_to_append = int(number_to_append)
                number_list.append(number_to_append)
                flag = True
            except ValueError:
                print("Must be an integer")
    return number_list


def calculate_average(a_list):
    """
    Takes in a list of numbers and calculates their average value
    :param a_list: required
    :return: float
    """
    total = 0
    average = 0
    for x in a_list:
        total += int(x)
    average = total/len(a_list)
    return average


if __name__ == '__main__':
    try:
        user_input = numbers_to_store()
        print("List of numbers: " + str(user_input))
        print("Average of numbers in list: " + str(calculate_average(user_input)))
    except ValueError as e:
        print(e)
