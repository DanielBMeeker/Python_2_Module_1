"""
Program: function_decorator.py
Author: Daniel Meeker
Date: 9/3/2020

This file demonstrates creating and using a decorator
to make a function run two times.
"""


def do_it_twice(func):  # decorator
    def wrapper():  # wrapper
        func()
        func()

    return wrapper


@do_it_twice  # using the decorator
def echo():
    print("Echo")


if __name__ == '__main__':
    echo()
