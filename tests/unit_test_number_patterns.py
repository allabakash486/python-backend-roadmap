import unittest
import sys
import os
import io
from contextlib import redirect_stdout
from unittest.mock import patch

from Learning.day_01.number_patterns import *


class TestNumberPatterns(unittest.TestCase):

    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(10), "even")
        self.assertEqual(even_or_odd(11), "odd")

    def test_largest_two_three(self):
        self.assertEqual(largest_of_two_numbers(20, 10), 20)
        self.assertEqual(largest_of_two_numbers(5, 5), "Both numbers are equal")
        self.assertEqual(largest_of_three_numbers(10, 20, 15), 20)

    def test_sum_and_swap(self):
        self.assertEqual(sum_of_two_numbers(10, 20), 30)
        self.assertEqual(swap_two_numbers(10, 20), (20, 10))

    def test_reverse_count_sum_product(self):
        self.assertEqual(reverse_number(12345), 54321)
        self.assertEqual(count_digits(12345), 5)
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(product_of_digits(12345), 120)

    def test_primes(self):
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(1))
        self.assertEqual(prime_numbers_up_to_n(10), [2, 3, 5, 7])
        self.assertEqual(first_n_primes(5), [2, 3, 5, 7, 11])
        self.assertEqual(nth_prime(1), 2)

    def test_prime_utils(self):
        self.assertEqual(prim_or_not(29), "prime")
        self.assertEqual(prime_or_not_(13), "prime")
        self.assertTrue(are_twin_primes(11, 13))
        self.assertEqual(prime_factors(60), [2, 2, 3, 5])

    def test_palindrome_and_related(self):
        self.assertTrue(is_palindrome(121))
        self.assertFalse(is_palindrome(123))
        self.assertEqual(palindrome_or_not(121), "palindrome")

    def test_sign_gcd_lcm_hcf(self):
        self.assertEqual(positive_negative_or_zero(10), "positive")
        self.assertEqual(positive_negative_or_zero(-1), "negative")
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(lcm(48, 18), 144)
        self.assertEqual(hcf(48, 18), 6)
        self.assertEqual(gcd_multiple_numbers(48, 18, 30), 6)

    def test_perfect_and_special_numbers(self):
        self.assertEqual(perfect_square_or_not(25), "perfect square")
        self.assertTrue(perfect_cube_or_not(27))
        self.assertTrue(is_happy_number(19))
        self.assertEqual(is_perfect_number(6), "perfect number")
        self.assertEqual(is_strong_number(145), "strong number")
        self.assertEqual(is_neon_number(9), "neon number")
        self.assertTrue(is_automorphic_number(25))
        self.assertEqual(is_spy_number(123), "spy number")
        self.assertEqual(is_duck_number(1023), "duck number")
        self.assertEqual(is_harshad_number(18), "harshad number")
        self.assertEqual(is_sunny_number(8), "sunny number")
        self.assertEqual(is_peterson_number(145), "peterson number")


if __name__ == "__main__":
    unittest.main(verbosity=2)