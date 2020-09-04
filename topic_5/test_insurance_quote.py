"""
Program: test_insurance_quote.py
Author: Daniel Meeker
Date: 9/3/2020

This file contains all the unit tests for testing
the insurance_quote.py program
"""
import unittest
from topic_5 import insurance_quote as iq


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = iq.Customer('Daniel Meeker', 31, 'F')  # Note the use of 'F' for Full Coverage

    def tearDown(self):
        del self.customer

    def test_initial_required_attributes(self):  # tests the constructor
        self.assertEqual(self.customer.customer_name, 'Daniel Meeker')
        self.assertEqual(self.customer.customer_age, 31)
        self.assertEqual(self.customer.coverage, 'F')

    def test_initial_all_attributes(self):
        customer = iq.Customer('Daniel Meeker', 31, 'SM', True, True)  # Note the use of 'SM' for State Minimum Coverage
        customer2 = iq.Customer('Daniel Meeker', 31, 'L')  # Note the use of 'L' for Liability Coverage
        self.assertEqual(customer.customer_name, 'Daniel Meeker')
        self.assertEqual(customer.customer_age, 31)
        self.assertEqual(customer.coverage, 'SM')
        self.assertEqual(customer2.coverage, 'L')
        self.assertTrue(customer.accident)
        self.assertTrue(customer.upfront)
        del customer, customer2

    def test_object_not_created_name_error(self):
        with self.assertRaises(ValueError):
            customer = iq.Customer(31, 31, 'SM')

    def test_object_not_created_age_error(self):
        with self.assertRaises(ValueError):
            customer = iq.Customer("Daniel Meeker", 15, 'L')

    def test_object_not_created_age_not_int(self):
        with self.assertRaises(AttributeError):
            customer = iq.Customer('Daniel Meeker', '31', 'L')

    def test_object_not_created_coverage_error(self):
        with self.assertRaises(ValueError):
            customer = iq.Customer('Daniel Meeker', 31, 'Full Coverage')

    def test_calculate_basic_coverage_16(self):
        customer1 = iq.Customer('Daniel Meeker', 16, 'SM')  # min age for base rate
        customer2 = iq.Customer('Daniel Meeker', 16, 'L')
        customer3 = iq.Customer('Daniel Meeker', 24, 'F')  # max age for base rate
        self.assertEqual(customer1.calculate_base_rate(), 2593)
        self.assertEqual(customer2.calculate_base_rate(), 2957)
        self.assertEqual(customer3.calculate_base_rate(), 6930)
        del customer1, customer2, customer3

    def test_calculate_basic_coverage_25(self):
        customer1 = iq.Customer('Daniel Meeker', 25, 'SM')  # min age for base rate
        customer2 = iq.Customer('Daniel Meeker', 25, 'L')
        customer3 = iq.Customer('Daniel Meeker', 34, 'F')  # max age for base rate
        self.assertEqual(customer1.calculate_base_rate(), 608)
        self.assertEqual(customer2.calculate_base_rate(), 691)
        self.assertEqual(customer3.calculate_base_rate(), 1745)
        del customer1, customer2, customer3

    def test_calculate_basic_coverage_35(self):
        customer1 = iq.Customer('Daniel Meeker', 35, 'SM')  # min age for base rate
        customer2 = iq.Customer('Daniel Meeker', 35, 'L')
        customer3 = iq.Customer('Daniel Meeker', 44, 'F')  # max age for base rate
        self.assertEqual(customer1.calculate_base_rate(), 552)
        self.assertEqual(customer2.calculate_base_rate(), 627)
        self.assertEqual(customer3.calculate_base_rate(), 1564)
        del customer1, customer2, customer3

    def test_calculate_basic_coverage_45(self):
        customer1 = iq.Customer('Daniel Meeker', 45, 'SM')  # min age for base rate
        customer2 = iq.Customer('Daniel Meeker', 45, 'L')
        customer3 = iq.Customer('Daniel Meeker', 54, 'F')  # max age for base rate
        self.assertEqual(customer1.calculate_base_rate(), 525)
        self.assertEqual(customer2.calculate_base_rate(), 596)
        self.assertEqual(customer3.calculate_base_rate(), 1469)
        del customer1, customer2, customer3

    def test_calculate_basic_coverage_55(self):
        customer1 = iq.Customer('Daniel Meeker', 55, 'SM')  # min age for base rate
        customer2 = iq.Customer('Daniel Meeker', 55, 'L')
        customer3 = iq.Customer('Daniel Meeker', 64, 'F')  # max age for base rate
        self.assertEqual(customer1.calculate_base_rate(), 494)
        self.assertEqual(customer2.calculate_base_rate(), 560)
        self.assertEqual(customer3.calculate_base_rate(), 1363)
        del customer1, customer2, customer3

    def test_calculate_basic_coverage_65(self):
        customer1 = iq.Customer('Daniel Meeker', 65, 'SM')  # min age for base rate
        customer2 = iq.Customer('Daniel Meeker', 65, 'L')
        customer3 = iq.Customer('Daniel Meeker', 129, 'F')  # max age for base rate
        self.assertEqual(customer1.calculate_base_rate(), 515)
        self.assertEqual(customer2.calculate_base_rate(), 585)
        self.assertEqual(customer3.calculate_base_rate(), 1402)
        del customer1, customer2, customer3

    def test_calculate_accident_rate(self):
        # accident rate calculated based off base rate
        # so since I have widespread testing of base rate
        # I felt that I only need to show that the accident
        # rate is correct one time
        customer1 = iq.Customer('Daniel Meeker', 31, 'F', True)
        self.assertEqual(customer1.calculate_accident_rate(), 2460.45)
        del customer1

    def test_calculate_upfront_discount(self):
        # upfront rate calculated based off base rate
        # so since I have widespread testing of base rate
        # I felt that I only need to show that the upfront
        # rate is correct one time
        customer1 = iq.Customer('Daniel Meeker', 31, 'F', False, True)
        self.assertEqual(customer1.calculate_upfront_discount(), 1570.5)
        del customer1

    def test_calculate_accident_and_upfront(self):
        customer1 = iq.Customer('Daniel Meeker', 31, 'F', True, True)
        self.assertEqual(customer1.calculate_upfront_discount(), 2214.4)


if __name__ == '__main__':
    unittest.main()
