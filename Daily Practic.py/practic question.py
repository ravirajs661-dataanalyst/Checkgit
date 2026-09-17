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



