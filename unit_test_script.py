from unittest import TestCase
from calculate_fraction import *


class Test(TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11)

    def test_add_fail(self):
        self.assertNotEqual(add(5, 6), 12)

    def test_subtract(self):
        self.assertEqual(subtract(15, 6), 9)

    def test_product(self):
        self.assertEqual(product(15, 6), 90)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)

    def test_mixed_to_improper_fraction(self):
        self.assertEqual(mixed_to_improper_fraction("1_3/4"), Fraction(7/4))

    def test_improper_fraction_to_mixed(self):
        self.assertEqual(improper_fraction_to_mixed(5,7), "0_5/7")
