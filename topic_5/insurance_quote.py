"""
Program: insurance_quote.py
Author: Daniel Meeker
Date: 9/2/2020

This program will allow a user to input the
desired coverage level and output the rate
which will be based on age of customer.
"""


class Customer:
    """
    Customer Class
    """

    def __init__(self, customer_name, customer_age, coverage, accident=False, upfront=False):
        """
        Constructor for customer class
        :param customer_name: required
        :param customer_age: required
        :param coverage: required
        :param accident: optional
        :param upfront: optional
        """
        coverage_levels = ['SM', 'L', 'F']
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")
        if not (name_characters.issuperset(str(customer_name))):
            raise ValueError("Must enter a name")
        self.customer_name = customer_name
        if isinstance(customer_age, int):
            if 16 <= customer_age < 130:  # the oldest human in recorded history was 122 so I rounded up to 130
                self.customer_age = customer_age
            else:
                raise ValueError("Customer must be older than 16")
        else:
            raise AttributeError("Customer Age must be an integer")
        if coverage.upper() in coverage_levels:
            self.coverage = coverage.upper()
        else:
            raise ValueError("Coverage must be either 'SM', 'L', or 'F'")
        self.accident = accident
        self.upfront = upfront

    def __str__(self):
        """
        overrides built-in function
        :return: a basic string to identify the object
        """
        return ("Customer: {self.customer_name}, {self.customer_age}, "
                "{self.coverage}".format(self=self))

    def __repr__(self):
        """
        overrides built-in function
        :return: a string that mimics the constructor.
        """
        return ("{self.__class__.__name__}('{self.customer_name}', {self.customer_age}, "
                "'{self.coverage}')".format(self=self))

    def display(self):
        """
        gathers all the info from the object to create a prettyfied string
        :return: a string
        """
        return ("Customer: {self.customer_name}\n"
                "Age: {self.customer_age}\n"
                "Coverage Level: {self.coverage}".format(self=self))

    def calculate_base_rate(self):
        """
        contains a dictionary of all the base coverage levels
        :return: the value of the key associated with the desired coverage
        """
        base_rate = {"16, SM": 2593, "16, L": 2957, "16, F": 6930,
                     "25, SM": 608, "25, L": 691, "25, F": 1745,
                     "35, SM": 552, "35, L": 627, "35, F": 1564,
                     "45, SM": 525, "45, L": 596, "45, F": 1469,
                     "55, SM": 494, "55, L": 560, "55, F": 1363,
                     "65, SM": 515, "65, L": 585, "65, F": 1402}
        age = self.customer_age
        if 16 <= age < 25:
            age = 16
        elif 25 <= age < 35:
            age = 25
        elif 35 <= age < 45:
            age = 35
        elif 45 <= age < 55:
            age = 45
        elif 55 <= age < 65:
            age = 55
        else:
            age = 65
        level = self.coverage
        return base_rate.get(str(age) + ", " + str(level))

    def calculate_accident_rate(self):
        """
        this function will calculate how much is added to the price
        if the person has had an accident
        :return: float
        """
        a_m = 1.41  # accident multiplier
        return round(self.calculate_base_rate() * a_m, 2)

    def calculate_upfront_discount(self):
        """
        this function will calculate the price if the person pays
        upfront to get the 10% discount
        :return: float
        """
        upfront_discount = .90
        if not self.accident:
            return round(self.calculate_base_rate() * upfront_discount, 2)
        else:
            return round(self.calculate_accident_rate() * upfront_discount, 2)


# Driver
if __name__ == '__main__':
    try:
        name = input("What is the customer name? ")
        customer_age = input("How old is the customer? ")
        coverage = input("Enter:\n'SM' for State Minimum coverage "
                         "\n'L' for Liability Coverage"
                         "\n'F' for Full Coverage\n")
        customer1 = Customer(name, int(customer_age), coverage)
        insurance_rate = {name: customer1.calculate_base_rate()}
        print(f'Base Rate: ${insurance_rate.get(name):.2f}')
        accident = input("Y/N customer has been in an accident?")
        if accident.upper() == 'Y':
            customer1.accident = True
            insurance_rate[name] = customer1.calculate_accident_rate()
            print(f'Accident Rate: ${insurance_rate.get(name):.2f}')
        upfront = input("Y/N customer wants to pay upfront?")
        if upfront.upper() == 'Y':
            customer1.upfront = True
            insurance_rate[name] = customer1.calculate_upfront_discount()
            print(f'Upfront Discount Rate: ${insurance_rate.get(name):.2f}')
        del customer1
    except ValueError as e:
        print(e)
    except AttributeError as e:
        print(e)
