""" 
Python Data Types - 30 Questions
Integer (int) Questions
Store an integer and print it.
Add two integers and display the result.
Subtract two integers.
Multiply two integers.
Find the quotient and remainder of two integers.
Check whether a number is even or odd.
Find the largest of two integers.
Find the largest of three integers.
Swap two integer variables without using a third variable.
Calculate the square and cube of an integer.
Float (float) Questions
Store a float value and print it.
Calculate the area of a circle.
Calculate simple interest.
Calculate compound interest.
Calculate the average of three float numbers.
String (str) Questions
Print your full name.
Find the length of a string.
Convert a string to uppercase.
Convert a string to lowercase.
Reverse a string.
Check whether a string is a palindrome.
Count the number of vowels in a string.
Count the number of consonants in a string.
Count the occurrence of a specific character in a string.
Replace a word in a string with another word.
Boolean (bool) Questions
Check whether a person is eligible to vote.
Check whether a number is positive.
Compare two numbers and print True or False.
List (list) Questions
Create a list of 10 numbers and find the largest element.
Create a list of 10 numbers and find the sum of all elements.
Additional Practice (Optional - Advanced)
Create a tuple and find its length.
Count the occurrences of an element in a tuple.
Remove duplicates from a list using a set.
Find the union of two sets.
Find the intersection of two sets.
Create a student dictionary and print all keys.
Create a student dictionary and print all values.
Add a new key-value pair to a dictionary.
Update an existing value in a dictionary.
Merge two dictionaries.
"""

#This file contains the implementations of the above questions. You can run this file to see the outputs for each question.

# Integer (int) Questions
def store_and_print_integer(num):
    return num
num = 10
print(store_and_print_integer(num))

def add_two_integers(a, b):
    return a + b
a, b = 10, 20
print(add_two_integers(a, b))

def subtract_two_integers(a, b):
    return a - b
a, b = 20, 10
print(subtract_two_integers(a, b))

def multiply_two_integers(a, b):
    return a * b
a, b = 10, 20
print(multiply_two_integers(a, b))

def quotient_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder
a, b = 20, 3
print(quotient_and_remainder(a, b))

def even_or_odd(num):
    return "even" if num % 2 == 0 else "odd"
num = 10
print(even_or_odd(num))

def largest_of_two_numbers(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"
a, b = 20, 10
print(largest_of_two_numbers(a, b))

def largest_of_three_numbers(a, b, c):
    return max(a, b, c)
a, b, c = 10, 20, 15
print(largest_of_three_numbers(a, b, c))

def swap_two_numbers(a, b):
    a, b = b, a
    return a, b
a, b = 10, 20
print(swap_two_numbers(a, b))


def square_and_cube(num):
    return num ** 2, num ** 3
num = 3
print(square_and_cube(num)) 

# Float (float) Questions
def store_and_print_float(num):
    return num
num = 3.14
print(store_and_print_float(num))

def area_of_circle(radius):
    import math
    return math.pi * radius ** 2
radius = 5
print(area_of_circle(radius))

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
principal, rate, time = 1000, 5, 2
print(simple_interest(principal, rate, time))


def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal
principal, rate, time = 1000, 5, 2  
print(compound_interest(principal, rate, time))


def average_of_three_floats(a, b, c):
    return (a + b + c) / 3
a, b, c = 1.5, 2.5, 3.5
print(average_of_three_floats(a, b, c))


# String (str) Questions
def print_full_name(first_name, last_name):
    return f"{first_name} {last_name}"
first_name, last_name = "John", "Doe"
print(print_full_name(first_name, last_name))


def length_of_string(s):
    return len(s)
s = "Hello, World!"
print(length_of_string(s))


def string_to_uppercase(s):
    return s.upper()
s = "hello"
print(string_to_uppercase(s))

def string_to_lowercase(s):
    return s.lower()
s = "HELLO"
print(string_to_lowercase(s))

def reverse_string(s):
    return s[::-1]
s = "Hello"
print(reverse_string(s))


def is_palindrome(s):
    return s == s[::-1]
s = "121"
print(is_palindrome(s))

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
s = "Hello, World!"
print(count_vowels(s))


def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)
s = "Hello, World!"
print(count_consonants(s))

def count_occurrence(s, char):
    return s.count(char)
s = "Hello, World!"
char = "o"
print(count_occurrence(s, char))

def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)
s = "Hello, World!"
old_word = "World"
new_word = "Python"
print(replace_word(s, old_word, new_word))  


# Boolean (bool) Questions
def is_eligible_to_vote(age):
    return age >= 18
age = 20
print(is_eligible_to_vote(age))


def is_positive(num):
    return num > 0
num = 10
print(is_positive(num))

def compare_numbers(a, b):
    return a > b
a, b = 10, 20
print(compare_numbers(a, b))

# List (list) Questions
def largest_in_list(lst):
    return max(lst)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(largest_in_list(lst))

def sum_of_list(lst):
    return sum(lst)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_list(lst))

#Tuple (tuple) Questions

def length_of_tuple(tpl):
    return len(tpl)
tpl = (1, 2, 3, 4, 5)
print(length_of_tuple(tpl))


def count_occurrence_in_tuple(tpl, element):
    return tpl.count(element)   
tpl = (1, 2, 3, 4, 5, 2)
element = 2
print(count_occurrence_in_tuple(tpl, element))

# Set (set) Questions
def remove_duplicates_from_list(lst):
    return list(set(lst))
lst = [1, 2, 3, 4, 5, 2, 3]
print(remove_duplicates_from_list(lst))

def union_of_sets(set1, set2):
    return set1.union(set2)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(union_of_sets(set1, set2))

def intersection_of_sets(set1, set2):
    return set1.intersection(set2)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(intersection_of_sets(set1, set2))

# Dictionary (dict) Questions
def print_dictionary_keys(dct):
    return list(dct.keys())
dct = {"name": "John", "age": 30, "city": "New York"}
print(print_dictionary_keys(dct))

def print_dictionary_values(dct):
    return list(dct.values())
dct = {"name": "John", "age": 30, "city": "New York"}
print(print_dictionary_values(dct))

def add_key_value_pair(dct, key, value):
    dct[key] = value
    return dct
dct = {"name": "John", "age": 30}
key = "city"
value = "New York"
print(add_key_value_pair(dct, key, value))

def update_dictionary_value(dct, key, value):
    if key in dct:
        dct[key] = value
    return dct
dct = {"name": "John", "age": 30}
key = "age"
value = 31
print(update_dictionary_value(dct, key, value))


def merge_dictionaries(dct1, dct2):
    return {**dct1, **dct2}
dct1 = {"name": "John", "age": 30}
dct2 = {"city": "New York", "country": "USA"}
print(merge_dictionaries(dct1, dct2))



