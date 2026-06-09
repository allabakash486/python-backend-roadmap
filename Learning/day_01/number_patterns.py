# This methode will verify whether the number is even or odd.
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    return "odd"
number = 10
result = even_or_odd(number)
print("The number", number, "is", result)

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

#this program will print whether the number is a perfect cube or not.
def perfect_cube_or_not(num):
    if num < 0:
        return "not a perfect cube"
    root = int(num ** (1/3))
    if root * root * root == num:
        return "perfect cube"
    return "not a perfect cube"
number = int(input("Enter a number: "))
result = perfect_cube_or_not(number)
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


#this program will print whether the number is a armstrong number or not.
def armstrong_or_not(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    if armstrong_sum == num:
        return "armstrong number"
    return "not an armstrong number"    

number = int(input("Enter a number: "))
result = armstrong_or_not(number)
print("The number", number, "is", result)


