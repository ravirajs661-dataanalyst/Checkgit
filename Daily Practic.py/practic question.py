# n=int(input("enter a number"))


# Print numbers from 1 to 20 using a for loop.
# for i in range(1,21):
#     print(i)

# Print all even numbers from 1 to 50 using a while loop.
# n=1
# while n<=50:
#     if n%2==0:
#         print(n)
#     n=n+1

# Take a number from the user and print its multiplication table from 1 to 10.
# n= int(input("enter a number"))
i=1
# while i<=10:
#     print(i*n)
#     i=i+1

# for i in range(1,11):
#     print(i*n)

# Take n from the user and find the sum of numbers from 1 to n
# n= int(input("enter a number"))
# total=0
# for i in range(i,n+1):
#     total+=i
# print("sum=",total)

# Take a number from the user and find its factorial using a loop.
# n= int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact= fact*i
# print(fact)

# Take a number from the user and reverse it using a while loop.
n = 12345
reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)

# n=int(input("enter a number"))
# # for i in range(1,11):
# #     print(n*i)

# while i<=10:
#     print(n*i)
#     i=i+1

# for i in range(1,5):
#     for j in range(1,4):
#         print(j)

# Print numbers from 1 to 100. Print Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both, otherwise print the number
# for i in range(1,51):
#     if i%3==0  and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

# Find the sum and average of a list without using sum() or statistics.mean().Uses: Lists, Loop, Variables.
mark=[85,75,40,31,28,38,57]
total=0
# for i in mark:
#     total=total+i
# print(total)

# avg=total/len(mark)
# print(avg)

# print(sum(mark))      #1st method

# Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

# Print numbers from 10 to 1.
# for i in range(10,0,-1):
#     print(i)

i=1
# while i<=10:
#     print(i)
#     i=i+1

a=10
# while a>=1:
#     print(a)
#     a=a-1

#print all even number 1 to 50.
n=1
# while n<=50:
#     if n%2==0:
#         print(n)
#     n=n+1

#print all odd number 1 to 50.
# while n<=50:
#    print(n)
#    n=n+2

# Print the multiplication table of a given number.
# n=int(input("enter a number"))
# i=1
# while i<=10:
#    print(n*i)
#    i=i+1

# Find the sum of numbers from 1 to 100.
i=1
total=0
# while i<=100:
#     total=total+i
#     i=i+1
# print(total)

# Find the sum of all even numbers from 1 to 100.
i = 1
total = 0
# while i<=100:
#     if i%2==0:
#         total=total+i
#     i=i+1
# print(total)

# Print the square of numbers from 1 to 10.
# for i in range(1,11):
#     print(i**2)

# Print the cube of numbers from 1 to 10.
# for i in range(1,11):
#     print(i**3)

# Print each character of a given string.
# name = "raviraj"
# i=0
# while i <len(name):
#     print(name[i])
#     i=i+1

# duplicate value kaise find kare.----Most Important Question----
items = [1,2,2,3,4,4,4,5,9,9]
dup=[]
# for i in items:
#     count=0
#     for j in items:
#         if i==j:
#             count=count+1
#     if count>1 and i not in dup:
#         dup.append(i)
# print(dup)

"""
students=("Ravi",26,"Bca",8.5)
name, age, course, gpa=students
print(name, age, course, gpa)

numbers= [1,2,3,4,5,6,7]
print(numbers)

"""

#------------- Iterator Example ------------ 
"""
list=[2,4,6,8,10,12]
it=iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

"""
"""
name="Ravi_raj"
it=iter(name)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

"""
"""
#  Practic File On studies file------
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
"""
"""
# Take a number and check whether it is positive, negative, or zero.
num=int(input("Enter a Number: "))
if num >0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("Zero")
"""
"""
# Take a person's age and print:
age=int(input("Enter age: "))
if age < 13:
    print("child")
elif age >13 and age<19:
    print("Tenager")
elif age >20 and age < 59:
    print("Adult")
else:
    print("Senior")
"""

"""
# Take three numbers and find the largest number without using max().
num=(3,5,7,9,14,52,2)
largest=0
for i in num:
    if i > largest:
        largest=i
print(largest)
"""
"""
# Create a simple calculator using match-case:
num1=int(input("Enrer first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter a operator: (+,-,*,/)")

while True:
    if operator == "+":
        print(num1 + num2)
        break
    elif operator == "-":
        print(num1 - num2)
        break
    elif operator == "*":
        print(num1 * num2)
        break
    elif operator == "/":
        print(num1 /num2)
        break
    else:
        print("Invalid Operator")
    break

"""
"""
# Part 2: Strings, Indexing & Slicing
text = "Python Programming"

print(text[0]) # print first index
print(text[:-2:-1]) # print last index
print(text[:7])  # print first 6 index
print(text[-11:]) # print last 11 cahrcter
print(text[::-1]) # Reverse Indexing
"""
"""
# Count the number of vowels in:
text = "Python Programming"
count=0
for i in text:
    if i in "aeiouAEIOU":
        count=count + 1
print(count)
"""
"""
# Take a string from the user and check whether it is a palindrome.
text = input("Enter a string: ")
reverse=text[::-1]

if text == reverse:
    print("Palindrone")
else:
    print("Not plaindrone")
"""
"""
# Create a new string where every space is replaced with _.
text = "data analysis"
print(text.replace(" ","_"))
"""
"""
# Take a full name from the user and print:
name=input("enter your name: ")
n=name.split()
print("First Name: ", n[0])
print("Last Name: ", n[-1])
"""
"""
# Find the sum of all elements using a loop, without sum().
numbers = [10, 20, 30, 40, 50]
total= 0
for i in numbers:
    total=total+i
print(total)
"""

"""
# Find the largest and smallest number in a list without using max() and min().
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest Number: ", largest)
print("Smallest Number: ", smallest)
"""
"""
# Remove duplicate values.
numbers = [10, 20, 10, 30, 20, 40, 10]
new_list=[]
for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)
"""
"""
# Create two sets:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(A|B)
print(A&B)
print(A-B)
print(A^B)
"""
"""
# Given a tuple: Print it in reverse order.
data = (10, 20, 30, 40, 50)
print(data[::-1])
"""
"""
# Create a dictionary containing: Print each key and value using a loop.
students={
    "name" : "ravi raj",
    "age" :22,
    "city" : "patna",
    "course" : "Python, sql, excel"
}

for key, value in students.items():
    print(key,":",value)
"""

# Find the subject with the highest marks without using max().
marks = {
    "Math": 85,
    "English": 72,
    "Python": 91,
    "SQL": 88
}

"""
# Create a dictionary containing 5 students and their marks. Print only students who scored 70 or more.
students={
    "Ravi": 85,
    "Priya": 70,
    "Neha": 55,
    "Nandni": 45,
    "Amit": 60
}

for name, marks in students.items():
    if marks > 50:
        print(name, marks)

"""
# Take a number from the user and check whether it is positive, negative, or zero.
# num=int(input("Enter a number: "))
# if num > 0:
#     print("Possitive number")
# elif num < 0:
#     print("Negative Number")
# else:
#     print("Zero")

# Take a number and print whether it is even or odd.
# num=int(input("Enter a number: "))
# if num % 2==0:
#     print("Even Numbr")
# else:
#     print("Odd Number")

# Take 3 numbers and print the largest number without using max().
# num=[50,38,67,28,49,19]
# largest=0
# for i in num:
#     if i > largest:
#         largest=i

# print(largest)

# Print the numbers from 1 to 50 using a for loop.
# for i in range(1,51):
#     print(i)

# Print all even numbers between 1 and 100.
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)

# Calculate the sum of numbers from 1 to 100.
# total=0
# for i in range(1,101):
#     total= total+i
# print(total)

# Take a number from the user and print its multiplication table.
# n = int(input("Enter a number"))
# for i in range(1,11):
#     print(n*i)

# Take a number and calculate its factorial.
# n = int(input("Enter a number"))
# total=1
# for i in range (1, n+1):
#     total=total*i

# print(total)

# Check whether a number is prime or not.
# n = int(input("Enter a number"))
# count=0
# while True:
#     for i in range(1,n+1):
#         if n % i ==0:
#             count=count+ 1

#     if count == 2:
#         print("Prime Number")
#         break
#     else:
#         print("Not Prime")
#     break

# Print all prime numbers between 1 and 100.
# for n in range(2,101):
#     count=0
#     for i in range(1, n+1):
#         if n % i== 0:
#             count= count+1

#     if count == 2:
#         print(n)

# # Reverse a number without converting it into a string.
# number = int(input("Enter a number"))
# reverse=0
# while number > 0:
#     digit = number%10
#     reverse= reverse*10+ digit
#     number= number//10

# print(reverse)

# Count how many digits are present in a number.
# number = 5788584
# count=0
# while number > 0:
#     number=number//10
#     count=count+1

# print(count)

# Create a list of 10 numbers and find: maxmum, minimum, sum, avg
# number=[23,45,67,89,34,23,15,75,58,36]
# max=number[0]
# min=number[0]
# sum=0

# for i in number:
#     if i > max:
#         max=i
# print(max)

# for i in number:
#     if i < min:
#         min=i
# print(min)

# for i in number:
#     sum = sum + i
# print(sum)
# avg=(sum/len(number))
# print(avg)

# Remove duplicate values from this list without using set().
# numbers = [10, 20, 10, 30, 20, 40, 30]
# unique=[0]

# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# Find the second-largest number in a list.
# numbers = [10, 20, 10, 30, 20, 40, 30]
# largest =numbers[0]
# second_largest=numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
#     elif i > second_largest and second_largest != largest:
#         second_largest = i
# print(second_largest)

# Count how many times each element occurs in a list.
# numbers = [10, 20, 10, 30, 20, 40, 30]
# count=[]
# for i in numbers:
#     total=0
#     for j in numbers:
#         if i == j:
#            total=total + 1
#     count.append(total)
# print(count)    
    
# Create a function is_prime(n) that returns True if the number is prime, otherwise False.
# def is_prime(number):
#     count=0
#     for i in range (1, number + 1):
#         if number % i == 0:
#             count= count + 1

#     if count == 2:
#         return True
#     else:
#        return False

# print(is_prime(11))
# print(is_prime(18))

# Create a function that accepts a list and returns the largest and smallest values.
# def find_value(number):
#     largest=number[0]
#     smallest=number[0]

#     for i in number:
#         if i > largest:
#             largest = i

#         if i < smallest:
#             smallest = i

#     return largest, smallest


# number = [45, 33, 57, 63, 39, 29, 40, 98]
# largest, smallest = find_value(number)
# print(largest)
# print(smallest)

# Create a function that accepts a string and returns the number of vowels.
# def vowel( word ):
#     count=0

#     for i in word:
#         if i in "aeiouAEIOU":
#             count=count+1
#     return(count)

# print(vowel("python programming"))

# Create a function using *args that returns the sum of all numbers.
# def add(*args):
#     total=0
#     for number in args:
#         total=total + number
#     print(total)

# add(10,20,30,40)

# Create a function using **kwargs that prints student information.
# def student(**details):
#     for key, value in details.items():
#         print(key, ":", value)

# student(name ="Ravi", age=23, course="python, sql excel")

# def company(**details):
#     for key, value in details.items():
#         print(key, ":", value)

# company(name ="Ravi raj", dept="sales", salary=35000)

"""
# Using lambda, calculate the square of every number in:
numbers = [1, 2, 3, 4, 5]
squre=map(lambda n: n**2, numbers)
print(list(squre))

# Using filter(), extract numbers greater than 50
numbers = [10, 55, 23, 78, 90, 45, 61]
check=filter(lambda n: n>10, numbers)
print(list(check))

# Using map(), convert: into their cubes.
numbers = [2, 4, 6, 8, 10]
cubes=map(lambda n: n**3, numbers)
print(list(cubes))

# Using reduce(), calculate the product of:
from functools import reduce
numbers=[1, 2, 3, 4, 5]
result= reduce(lambda a,b: a+b, numbers)
print(result)
"""

"""
# Create a BankAccount class with: account holder, balance
class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def deposite(self, amount):
        self.balance = self.balance+ amount
        print("Deposited :", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdraw :", amount)
        else:
            print("Insufficent Balance!")

    def show_balance(self):
        print("Account Holder: ", self.name)
        print("Balance: ", self.balance)

account1=BankAccount("Ravi Raj", 50000)
account1.deposite(3000)
account1.withdraw(1000)
account1.show_balance()
"""
"""
# Create a Student class with: Create a method that calculates the percentage and displays whether the student Pass/Fail.
class students:
    def __init__(self, name, rool_no, mark):
        self.name=name
        self.rool_no=rool_no
        self.mark=mark

    def result(self):
        total=sum(self.mark)
        percentage=total / 5

        print("Name: ", self.name)
        print("Rool No: ", self.rool_no)
        print("Mark: ", self.mark)

        if percentage >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

student1= students("Ravi Raj", 101, [70,30,50,60,85])
student1.result()
"""
"""
class employeee:
    def __init__(self, name, salary, dept):
        self.name=name
        self.salary= salary
        self.dept= dept

    def __str__(self):
        return f"Name: {self.name}, \nSalary: {self.salary}, \nDepartment: {self.dept}"

emp1=employeee("Ravi Raj", 35000, "Sales")
print(emp1)
"""

# def greet():
#     print("Hello Ravi")

# greet()
# greet()

# Create a function add(a, b) that returns the sum of two numbers.
# def add(a,b):
#     print(a+b)

# add(10,15)

# Create a function student_info(name, age, course) that prints all student details.
# def student_info(name, age, course):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Course :", course)

# student_info("Ravi Raj", 23,"Python, sql, excel")

# Create a function that accepts two numbers and returns:
# def return_value(num1, num2):
#     print("Sum: ", num1 + num2)
#     print("Difference : ", num1 - num2)
#     print("Multiplication :", num1 * num2)
#     print("Division : ", num1 / num2)

# return_value(15, 5)

# Create function : return total salary
# def calculate_salary(salary, bonus=5000):
#     total_salary=salary + bonus
#     return total_salary

# print(calculate_salary(30000))
# print(calculate_salary(35000,10000))

# Create check_number(n) that returns: even and odd
# def check_number(n):
#     if n % 2 ==0:
#         return ('even:', n)
#     else:
#         return ('odd:', n)

# print(check_number(5))

# create: It should return True or False.
# def is_prime(number):
#     count=0
#     for i in range(1, number+1):
#         if number % i == 0:
#             count=count + 1

#     if count == 2:
#         return True
#     else:
#         return False

# print(is_prime(5))
# Create a function that accepts a list and returns: maximum, minimum, sum,avg
# def list_value(number):
#     maximum=number[0]
#     minimum=number[0]
#     total=0

#     for i in number:
#         if i > maximum:
#             maximum=i

#         if i<minimum:
#             minimum=i

#         total=total+i

#     avg=total/len(number)

#     return maximum,minimum,total,avg

# number=[10,20,30,40,50,60,70]

# maximum,minimum,total,avg=list_value(number)

# print(maximum)
# print(minimum)
# print(total)
# print(avg)

# Sum Using *args
# def total(*args):
#     total=0
#     for i in args:
#         total=total+i
#     return total

# print(total(10,20,30,40))

# Create a function using *args that finds the largest number.
# def max_value(*number):
#     largest=0
#     for i in number:
#         if i > largest:
#             largest=i
#     return largest

# print(max_value(50,49,70,20,59,99))

# Create a function using *args that tells how many arguments were passed.
# def count_value(*number):
#     count=0
#     for i in number:
#         count=count+1
#     return count

# print(count_value(30,4,5,6,7,8))

# Create a function that accepts any number of numbers and calculates their average.
# def avg_value(*number):
#     total=0
#     for i in number:
#         total=total+i
#     return total/len(number)

# print(avg_value(2,3,4,5,6,7))

# crate def students(**kwargs) Print all information.
# def students(**details):
#     for key, value in details.items():
#         print(key ,":", value)

# students(
#     name='Ravi Raj',
#     age=23,
#     course="SQL, Python, Excel",
#     city="Patna"
# )

# It should accept any employee information and print it.
# def employees(**details):
#     for key, value in details.items():
#         print(key,":", value)

# employees(
#     name="Ravi raj",
#     department="Sales",
#     salary="45000"
# )

# Create a function that tells how many keyword arguments were passed.
# def count_lenght(**details):
#     print(len(details))

# count_lenght(
#     name="Ravi raj",
#     age=23,
#     course="sql, python",
#     city="patna"
# )

# Create a function using **kwargs that searches for the salary value.
# def count_lenght(**details):
#     if "salary" in details:
#         print("Salary:", details["salary"])
#     else:
#         print("salary not found!")

# count_lenght(
#     name="Ravi raj",
#     age=23,
#     course="sql, python",
#     city="patna",
#     salary=45000
# )
  
# create: Print the positional and keyword arguments separately.
# def information(*marks, **details):
#     print("Marks: ", marks)
#     print("Details: ", details)

# information(
#     65,55,87,75,
#     name="Ravi Raj",
#     Class="Bs.c",
#     Age= 23,
#     Course="Computer Science"
# )


