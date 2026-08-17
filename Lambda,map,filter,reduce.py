#                               ------------Lambda Functio ------------

# Lambda function Python ka ek small/short function hota hai, jise hum usually tab use karte hain 
#          jab function ka kaam simple ho aur humein alag se def likhne ki zarurat na ho.
# square=lambda n:n*n
# print(square(5))

# check=lambda n:n%2==0
# print(check(10)) #True
# print(check(17)) #False

# multiply=lambda a,b:a*b
# print(multiply(10,5))

# Create a lambda function that takes a number and returns its square.
# square=lambda n:n*n
# print(square(5))

# Create a lambda function that takes a number and returns True if the number is even, otherwise False.
# n=int(input("Enter a number: "))
# check=lambda n:n%2==0

# print(check(n))

# Create a lambda function that takes two numbers and returns the larger number.
# largest=lambda a,b:a if a > b else b

# print(largest(10,17))

# Create a lambda function that takes price and quantity and returns the total amount.
# value=lambda price,quantity: price*quantity
# print(value(350,5))

# Create a lambda function that takes a string and returns the length of the string.
# length=lambda str: len(str)
# print(length("RaviRaj"))

#                        -------- Map Function --------

# Use map() and lambda to multiply every number by 2.
# numbers=[1,2,3,4,5,6]
# result= map(lambda n:n*2,numbers)

# print(list(result))

# Use map() to find the square of every number.
# numbers=[2,3,4,5,6]
# square=map(lambda n:n*n, numbers)
# print(list(square))

# Use map() to add 10 to every number.
# numbers=[5,10,15,20,25]
# result=map(lambda n:n+10, numbers)
# print(list(result))

# Convert Strings to Integers
# number=["10", "20", "30", "40"]
# convert=map(int,number)
# print(list(convert))

# Convert Names to Uppercase
# name=["raviraj","priya","neha","nandni"]
# upper=map(lambda n:n.upper(),name)
# print(list(upper))

#                       -------- Filter Function -------

# Use filter() and lambda to get only even numbers.
# number=[1,2,3,4,5,6]
# even=filter(lambda n:n%2==0 , number)
# print(list(even))

# Use filter() to get numbers greater than 10.
# number=[5,12,8,15,20,3,17,9,3,21]
# result=filter(lambda n:n>=10, number)
# print(list(result))

# Use filter() to get only positive numbers.
# number= [-5, 10, -2, 7, -8, 3]
# possitive=filter(lambda n:n>0, number)
# print(list(possitive))

# Use filter() and lambda to select names whose length is greater than 4.
# name=["Raviraj","Priya","nandni","Raj","Pri"]
# result=filter(lambda n:len(n)>4,name)
# print(list(result))

# Use filter() to select numbers that are divisible by 5.
# number=[10, 12, 15, 22, 25, 31, 40]
# result=filter(lambda n:n%5==0, number)
# print(list(result))

#              -------- Reduce Function -----------

# reduce() ka use multiple values ko combine karke ek single value banane ke liye hota hai.

from functools import reduce

number=[1,2,3,4,5]

result= reduce(lambda a,b:a+b, number)
print(result)










#               -------- Practic Question ----------
# Create a lambda function that takes a number and returns its cube.
# n=int(input("Enter a number: "))
# cube=lambda n:n**3
# print(cube(n))

# Create a lambda function that takes two numbers and returns their multiplication.
# multiplay=lambda a,b:a*b
# print(multiplay(10,5))

# Create a lambda function that returns True if a number is positive, otherwise False.
# n=int(input("Enter a number: "))
# check=lambda n: True if n>0 else False
# print(check(n))

# Use map() and lambda to add 5 to every number.
# number=[10,20,30,40]
# result=map(lambda n:n+5,number)
# print(list(result))

# Cube with lambda
# cube=lambda n:n**3
# print(cube(4))

# num=[2,3,4,5,6]
# cube=map(lambda n:n**3, num)
# print(list(cube))

# Upper case convert
# name=["python","sql","excel"]
# result=map(lambda n:n.upper(), name)

# print(list(result))

# filter the odd number. give number 1 to 20 find only odd number
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd=filter(lambda n:n%2!=0,num)
print(list(odd))
