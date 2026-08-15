#  *args ka use function mein multiple positional arguments lene ke liye hota hai.

# def add(*args):
#     print(args)

# add(10,20,30)

# Real life example in *args
# def add(*number):
#     total = 0
#     for i in number:
#         total=total+i
#     print(total)

# add(10, 20, 14, 25, 26, 48)
# add(10, 20 ,14,25,26,48)

# Create a function square() that takes a number and returns its square.
# def square(n):
#     return(n*n)

# # print(square(5))

# Create a function add() that takes two numbers and returns their sum.
# n1=int(input("Enter a number"))
# n2=int(input("Enter a number"))

# def add(n1,n2):
#     print(n1 + n2)

# add(n1,n2)

# Create a function sum_numbers(*args) that accepts any number of numbers and returns their total.
# def sum_numbers(*number):
#     total=0
#     for i in number:
#         total=total+i
#     print(total)

# sum_numbers(12,37,84,92)

# Create a function find_max(*args) that accepts any number of numbers and finds the maximum number.
# def find_max(*number):
#     return max(number)

# max=find_max(34,85,98,109)
# print(max)

# Create a function count_numbers(*args) that counts how many numbers were passed.
# def count_numbers(*number):
#     count=0
#     for i in number:
#         count=count+1
#     print(count)

# count_numbers(10, 20, 30, 40)

# Create a function even_numbers(*args) that accepts multiple numbers and prints only the even numbers.
# def even_numbers(*numbers):
#     for i in numbers:
#         if i%2==0:
#             print(i)

# even_numbers(10, 15, 20, 25, 30)

# Create a function average(*args) that accepts any number of numbers and calculates their average.
# def average(*numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     print((total)/len(numbers))

# average(10, 20, 30, 40)

# Create a function student(**kwargs) that accepts student information and prints all the details.
# def student(**kwargs):
#     print(kwargs)

# student(name="Ravi", age=26, city="Patna")

# Create a function employee(**kwargs) that prints the employee's name and salary.
def employees(**employee):
    print(name, salary=25000)


