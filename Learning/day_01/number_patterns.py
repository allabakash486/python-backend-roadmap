"""Beginner Number Programs
Check if a number is even or odd.
Find the largest of two numbers.
Find the largest of three numbers.
Check whether a number is positive, negative, or zero.
Calculate the sum of two numbers.
Swap two numbers.
Reverse a number.
Count digits in a number.
Find the sum of digits of a number.
Find the product of digits.
Prime Number Programs
Check if a number is prime.
Print all prime numbers from 1 to N.
Find the sum of prime numbers in a range.
Print the first N prime numbers.
Find the nth prime number.
Check if two numbers are twin primes.
Find prime factors of a number.
Palindrome & Reverse Programs
Check if a number is a palindrome.
Reverse a number.
Check if a number remains the same after reversal.
Find palindrome numbers in a range.
Armstrong Number Programs
Check if a number is an Armstrong number.
Print Armstrong numbers in a range.
Find the count of Armstrong numbers between two numbers.
Factorial Programs
Find the factorial of a number.
Find factorial using recursion.
Find factorial without using loops.
Sum of factorials from 1 to N.
Fibonacci Programs
Print Fibonacci series.
Print first N Fibonacci numbers.
Find nth Fibonacci number.
Check if a number belongs to Fibonacci series.
Perfect Number Programs
Check if a number is a perfect number.
Print all perfect numbers in a range.
Find the sum of perfect numbers.
Strong Number Programs
Check if a number is a Strong Number.
Print Strong Numbers in a range.
Special Number Programs
Check if a number is a Neon Number.
Check if a number is an Automorphic Number.
Check if a number is a Spy Number.
Check if a number is a Duck Number.
Check if a number is a Harshad Number.
Check if a number is a Sunny Number.
Check if a number is a Peterson Number.
Check if a number is a Disarium Number.
Check if a number is a Happy Number.
GCD & LCM Programs
Find GCD of two numbers.
Find LCM of two numbers.
Find HCF using Euclid's algorithm.
Find GCD of multiple numbers."""

# This methode will verify whether the number is even or odd.
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    return "odd"
number = 10
result = even_or_odd(number)
print("The number", number, "is", result)

#This program will find the largest of two numbers.
def largest_of_two_numbers(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    return "Both numbers are equal"
num1 = 10
num2 = 20
result = largest_of_two_numbers(num1, num2)
print("The largest of", num1, "and", num2, "is:", result)


#This program will find the largest of three numbers.
def largest_of_three_numbers(a, b, c):  
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c
num1 = 10
num2 = 20
num3 = 15
result = largest_of_three_numbers(num1, num2, num3)
print("The largest of", num1, ",", num2, "and", num3, "is:", result)


#This program will calculate the sum of two numbers.
def sum_of_two_numbers(a, b):
    return a + b
num1 = 10
num2 = 20       
result = sum_of_two_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)


#This program will swap two numbers.
def swap_two_numbers(a, b):
    return b, a
num1 = 10
num2 = 20
num1, num2 = swap_two_numbers(num1, num2)
print("After swapping: num1 =", num1, "num2 =", num2)


#This program will reverse a number.
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
number = 12345
result = reverse_number(number)
print("The reverse of", number, "is:", result)

#This program will count the digits in a number.
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
number = 12345
result = count_digits(number)
print("The number of digits in", number, "is:", result)

#This program will find the sum of digits of a number.
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total    
number = 12345
result = sum_of_digits(number)
print("The sum of digits in", number, "is:", result)

#This program will find the product of digits of a number.
def product_of_digits(num):
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10
    return product 
number = 12345
result = product_of_digits(number)
print("The product of digits in", number, "is:", result)


#This program will check if a number is prime or not.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = 29
result = is_prime(number)
if result:
    print("The number", number, "is prime.")
else:
    print("The number", number, "is not prime.")

#this program will print whether the number is prime or not.
def prim_or_not(num):
    if num <= 1:
        return "not prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "not prime"
    return "prime"
number = int(input("Enter a number: ")) 
result = prim_or_not(number)
print("The number", number, "is", result)


#this program will print whether the number is a prime number or not.
def prime_or_not_(num):
    if num <= 1:
        return "not prime"
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            return "not prime"
    return "prime"
number = int(input("Enter a number: "))
result = prime_or_not_(number)
print("The number", number, "is", result)

#This program will print all prime numbers from 1 to N.
def prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes
N = 50
result = prime_numbers_up_to_n(N)
print("Prime numbers from 1 to", N, "are:", result) 


#This program will find the sum of prime numbers in a range.
def sum_of_primes_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total
start = 1
end = 50
result = sum_of_primes_in_range(start, end)
print("The sum of prime numbers from", start, "to", end, "is:", result)


#This program will print the first N prime numbers.
def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
N = 10
result = first_n_primes(N)
print("The first", N, "prime numbers are:", result)


#This program will find the nth prime number.
def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num
N = 10
result = nth_prime(N)
print("The", N, "th prime number is:", result)

#This program will check if two numbers are twin primes.
def are_twin_primes(num1, num2):
    if abs(num1 - num2) == 2 and is_prime(num1) and is_prime(num2):
        return True
    return False
number1 = 11
number2 = 13
result = are_twin_primes(number1, number2)
if result:
    print("The numbers", number1, "and", number2, "are twin primes.")
else:
    print("The numbers", number1, "and", number2, "are not twin primes.")


#This program will find the prime factors of a number.
def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors
number = 60
result = prime_factors(number)
print("The prime factors of", number, "are:", result)

#This program will check if a number is a palindrome or not.
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
number = 12321
result = is_palindrome(number)
if result:
    print("The number", number, "is a palindrome.")
else:
    print("The number", number, "is not a palindrome.") 

#This program will reverse a number.
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
number = 12345
result = reverse_number(number)
print("The reverse of", number, "is:", result)


#This program will check if a number remains the same after reversal.
def is_same_after_reversal(num):
    return num == reverse_number(num)
number = 12321
result = is_same_after_reversal(number)
if result:
    print("The number", number, "remains the same after reversal.")
else:
    print("The number", number, "does not remain the same after reversal.")


#This program will find palindrome numbers in a range.
def palindrome_numbers_in_range(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes
start = 1
end = 100
result = palindrome_numbers_in_range(start, end)
print("Palindrome numbers from", start, "to", end, "are:", result)  


#This program will check if a number is an Armstrong number or not.
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num
number = 153
result = is_armstrong(number)   
if result:
    print("The number", number, "is an Armstrong number.")
else:
    print("The number", number, "is not an Armstrong number.")


#This program will print Armstrong numbers in a range.
def armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
start = 1
end = 1000
result = armstrong_numbers_in_range(start, end)
print("Armstrong numbers from", start, "to", end, "are:", result)

#This program will find the count of Armstrong numbers between two numbers.
def count_armstrong_numbers_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_armstrong(num):
            count += 1
    return count
start = 1
end = 1000
result = count_armstrong_numbers_in_range(start, end)
print("The count of Armstrong numbers from", start, "to", end, "is:", result)


#This program will find the factorial of a number.
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
number = 5
result = factorial(number)  
print("The factorial of", number, "is:", result)


#This program will find the factorial of a number using recursion.
def factorial_recursive(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)
number = 5
result = factorial_recursive(number)    
print("The factorial of", number, "is:", result)


#This program will find the factorial of a number without using loops.
def factorial_without_loops(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_without_loops(n - 1)
number = 5
result = factorial_without_loops(number)
print("The factorial of", number, "is:", result)


#This program will find the sum of factorials from 1 to N.
def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
N = 5
result = sum_of_factorials(N)
print("The sum of factorials from 1 to", N, "is:", result)

#This program will print the Fibonacci series.
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
N = 10
result = fibonacci_series(N)
print("The first", N, "numbers in the Fibonacci series are:", result)


#This program will print the first N Fibonacci numbers.
def first_n_fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
N = 10
result = first_n_fibonacci(N)
print("The first", N, "Fibonacci numbers are:", result)

#This program will find the nth Fibonacci number.
def nth_fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
N = 10
result = nth_fibonacci(N)   
print("The", N, "th Fibonacci number is:", result)




#This number will print whether the number is positive, negative or zero.
def positive_negative_or_zero(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    return "zero"
number = int(input("Enter a number: "))
result = positive_negative_or_zero(number)
print("The number", number, "is", result)

#This program will find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = 48
num2 = 18
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)


#This program will find the LCM of two numbers.
def lcm(a, b):
    return abs(a * b) // gcd(a, b) 
num1 = 48
num2 = 18
result = lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is:", result)


#This program will find the HCF of two numbers using Euclid's algorithm.
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a    
num1 = 48
num2 = 18
result = hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is:", result)


#This program will find the GCD of multiple numbers.
def gcd_multiple_numbers(*args):
    from math import gcd
    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result
numbers = [48, 18, 30]
result = gcd_multiple_numbers(*numbers)
print("The GCD of", numbers, "is:", result)


#This program will check if a number is a perfect square or not.
def perfect_square_or_not(num):
    if num < 0:
        return "not a perfect square"
    root = int(num**0.5)
    if root * root == num:
        return "perfect square"
    return "not a perfect square"
number = int(input("Enter a number: "))
result = perfect_square_or_not(number)
print("The number", number, "is", result)


#This program will check if a number is a perfect cube or not.
def perfect_cube_or_not(num):
    root = round(num ** (1/3))

    if root ** 3 == num:
        return True
    return False
number = int(input("Enter a number: "))
result = perfect_cube_or_not(number)
print("The number", number, "is", result)


#This program will check if a number is a palindrome or not.
def palindrome_or_not(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return "palindrome"
    return "not a palindrome"
number = int(input("Enter a number: "))
result = palindrome_or_not(number)
print("The number", number, "is", result)


#This program will check if a number is a happy number or not.
def is_happy_number(num):
    def get_next(n):
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit ** 2
            n //= 10
        return total_sum
    
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = get_next(num)
    
    return num == 1
number = int(input("Enter a number: "))
result = is_happy_number(number)
if result:
    print("The number", number, "is a happy number.")
else:
    print("The number", number, "is not a happy number.")


#This program will check if a number is a perfect number or not.
def is_perfect_number(num):
    if num < 1:
        return "not a perfect number"
    total = sum(i for i in range(1, num) if num % i == 0)
    if total == num:
        return "perfect number"
    return "not a perfect number"
number = int(input("Enter a number: "))
result = is_perfect_number(number)
print("The number", number, "is", result)


#This program will check if a number is a strong number or not.
def is_strong_number(num):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    total = sum(factorial(int(digit)) for digit in str(num))
    if total == num:
        return "strong number"
    return "not a strong number"
number = int(input("Enter a number: "))
result = is_strong_number(number)
print("The number", number, "is", result)


#This program will check if a number is a neon number or not.
def is_neon_number(num):
    square = num ** 2
    digit_sum = sum(int(digit) for digit in str(square))
    if digit_sum == num:
        return "neon number"
    return "not a neon number"
number = int(input("Enter a number: "))
result = is_neon_number(number)
print("The number", number, "is", result)

#This program will check if a number is an automorphic number or not.
def is_automorphic_number(num):
    square = num ** 2
    return str(square).endswith(str(num))
number = int(input("Enter a number: "))
result = is_automorphic_number(number)
if result:
    print("The number", number, "is an automorphic number.")
else:
    print("The number", number, "is not an automorphic number.")

#This program will check if a number is a spy number or not.
def is_spy_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    digit_product = 1
    for digit in str(num):
        digit_product *= int(digit)
    if digit_sum == digit_product:
        return "spy number"
    return "not a spy number"
number = int(input("Enter a number: "))
result = is_spy_number(number)
print("The number", number, "is", result)


#This program will check if a number is a duck number or not.
def is_duck_number(num):
    num_str = str(num)
    if '0' in num_str and not num_str.startswith('0'):
        return "duck number"
    return "not a duck number"
number = int(input("Enter a number: "))
result = is_duck_number(number)
print("The number", number, "is", result)


#This program will check if a number is a harshad number or not.
def is_harshad_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    if digit_sum != 0 and num % digit_sum == 0:
        return "harshad number"
    return "not a harshad number"
number = int(input("Enter a number: "))
result = is_harshad_number(number)
print("The number", number, "is", result)

#This program will check if a number is a sunny number or not.
def is_sunny_number(num):
    next_num = num + 1
    root = int(next_num ** 0.5)
    if root * root == next_num:
        return "sunny number"
    return "not a sunny number"
number = int(input("Enter a number: "))
result = is_sunny_number(number)
print("The number", number, "is", result)


#This program will check if a number is a peterson number or not.
def is_peterson_number(num):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    digit_factorial_sum = sum(factorial(int(digit)) for digit in str(num))
    if digit_factorial_sum == num:
        return "peterson number"
    return "not a peterson number"
number = int(input("Enter a number: "))
result = is_peterson_number(number)
print("The number", number, "is", result)

#This program will check if a number is a disarium number or not.
def is_disarium_number(num):
    num_str = str(num)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    if total == num:
        return "disarium number"
    return "not a disarium number"
number = int(input("Enter a number: "))
result = is_disarium_number(number)
print("The number", number, "is", result)




#this program will print whether the number is a perfect square or not.
def perfect_square_or_not(num):
    if num < 0:
        return "not a perfect square"
    root = int(num**0.5)
    if root * root == num:
        return "perfect square"
    return "not a perfect square"
number = int(input("Enter a number: "))
result = perfect_square_or_not(number)
print("The number", number, "is", result)



#this program will print whether the number is a palindrome or not.
def palindrome_or_not(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return "palindrome"
    return "not a palindrome"   
number = int(input("Enter a number: "))
result = palindrome_or_not(number)
print("The number", number, "is", result)



