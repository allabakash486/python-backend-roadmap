#This is a simple program to calculate the sum of two numbers and the difference between them.
def sum_of_two_numbers(a, b):
    return a + b
num1 = 5
num2 = 10
result = sum_of_two_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)



# This is a simple program to calculate the difference between two numbers.
def deduct_two_numbers(a, b):
    return a - b
result = deduct_two_numbers(num1, num2)
print("The difference between", num1, "and", num2, "is:", result)



#This is a simple program to calculate the product of two numbers.
def product_of_two_numbers(a, b):
    return a * b
result = product_of_two_numbers(num1, num2)
print("The product of", num1, "and", num2, "is:", result)



#This is a simple program to calculate the quotient of two numbers.
def quotient_of_two_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
result = quotient_of_two_numbers(num1, num2)
print("The quotient of", num1, "and", num2, "is:", result)  



#This is a simple program to calculate the remainder of two numbers.
def remainder_of_two_numbers(a, b): 
    if b != 0:
        return a % b
    else:
        return "Cannot divide by zero"
result = remainder_of_two_numbers(num1, num2)
print("The remainder of", num1, "and", num2, "is:", result)  


#this is a simple program to calculate the power of two numbers.
def power_of_two_numbers(a, b):
    return a ** b
result = power_of_two_numbers(num1, num2)
print("The power of", num1, "and", num2, "is:", result)


#This is a simple program to calculate the square root of a number.
def square_root_of_a_number(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Cannot calculate the square root of a negative number"  
result = square_root_of_a_number(num1)
print("The square root of", num1, "is:", result)

#this is a simple program to calculate the cube root of a number.
def cube_root_of_a_number(a):
    if a >= 0:
        return a ** (1/3)
    else:
        return "Cannot calculate the cube root of a negative number"
result = cube_root_of_a_number(num1)
print("The cube root of", num1, "is:", result)






def simple_sum(a,b):
    return a + b
a= 10
b=20
result = simple_sum(a,b)
print(f"sum of the two numbers {a} + {b} = {result}")
