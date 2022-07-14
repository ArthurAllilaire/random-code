from email.quoprimime import quote
import unittest
import csv
from tax_calc import *

class TestTaxes(unittest.TestCase):
    def setUp(self):
        #CSV csvfile with test cases
        with open('tax_calculator/tax_test_cases.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            fields = next(csvreader)
            print(fields)
            for row in csvreader:
                
                print(row)


        self.TAX_TYPES = ["INCOME TAX", "CORPORATION TAX", "NIC"]
        self.taxes = get_taxes("tax_calculator/tax_brackets.txt")

    def test_tax(self):
        tax = calc_tax(taxes, self.TAX_TYPES[0], self.incomes[1])

if __name__ == '__main__':
    unittest.main()