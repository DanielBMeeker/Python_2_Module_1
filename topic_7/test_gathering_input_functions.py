"""
Program: test_gathering_input_functions.py
Author: Daniel Meeker
Date: 9/3/2020

This file tests the functions from gathering_input_functions.py
Because I used a flag and while loops in my main file I could
not complete the unittests as instructed because they just
created infinite loops waiting for correct input to be entered.
My google searching on the subject said there is not a good way
to do unittesting when using a while loop without completely redoing
the logic of my assignment. I compromised and added a sentinel value
that will raise an error if used when deciding how many numbers to enter
so that I could show I know how to write the unittest with mocking input
to raise an error.
"""
import unittest
import unittest.mock as mock
from topic_7 import gathering_input_functions as gif


class MyTestCase(unittest.TestCase):
    def test_how_many_numbers_error(self):
        with mock.patch('builtins.input', return_value='x'):
            with self.assertRaises(ValueError):
                gif.how_many_numbers()

    def test_numbers_to_store(self):
        with mock.patch('builtins.input', side_effect=[3, 1, 2, 3]):
            self.assertEqual([1, 2, 3], gif.numbers_to_store())

    def test_calculate_average(self):
        a_list = [1, 2, 3, 4, 5]
        self.assertEqual(3.0, gif.calculate_average(a_list))


if __name__ == '__main__':
    unittest.main()
