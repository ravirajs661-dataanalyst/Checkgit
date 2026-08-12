# Take a number from the user and check whether it is even or odd.
# n= int(input("Enter a number: "))
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")

# Take a number n and print numbers from 1 to n using a for loop.
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i)

# Take a number n and find the sum of numbers from 1 to n.
# n= int(input("Enter a number: "))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print(total)

# Take a number from the user and print its multiplication table from 1 to 10.
# n= int(input("Enter a number: "))
# for i in range(1,11):
#     print(n*i)

# Take a number n and print all even numbers from 1 to n.
# n= int(input("Enter a number: "))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

# Create a list: Print all elements using a for loop.
numbers=[10,20,30,40,50]
# for i in numbers:
#     print(i)

# From the above list, find the sum of all elements using a loop.
total=0
# for i in numbers:
#     total=total+i
# print(total)

# Create a list of numbers and count how many even numbers are present.
numbers=[2,3,5,7,6,12,15,17,18,22,23,57,4,54]
# count=0
# for i in numbers:
#     if i%2==0:
#         count=count+1
# print(count)

# Create a list of numbers and count how many numbers are greater than 10.
numbers = [5, 12, 8, 20, 15, 3, 25, 7]
count=0
# for i in numbers:
#     if i>10:
#         count=count+1
# print(count)

# Create a list:Check whether 30 is present in the list.
numbers = [10, 20, 30, 40, 50]
# for i in numbers:
#     if i==30:
#         print("30 is present")

# Create a tuple:Print all elements using a loop.
numbers = (10, 20, 30, 40, 50)
# for i in numbers:
#     print(i)

# Find the largest number in a tuple without using max().
largest=numbers[0]
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)

# Create two sets:Find their union.
a={1,2,3,4}
b={3,4,5,6}
# new_set=a.union(b)
# print(new_set)

# Find the common elements between sets A and B.
n = a.intersection(b)
# print(n)

# Given:Remove duplicate values using a set.
numbers = [10, 20, 10, 30, 20, 40]
# n=list(set(numbers))
# print(n)

# Take 5 numbers from the user, store them in a list, and print separately:
# Even numbers
# Odd numbers

numbers=[]
even=[]
odd=[]

# for i in range(5):
#     n=int(input("Enter a number: "))
#     numbers.append(n)

# for i in numbers:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)

# print("even number: ", even)
# print("odd number: ", odd)

# Create a list of 5 numbers and use a for loop to print each number.
number=[12,15,8,20,30]
# for i in number:
#     print(i)

# Create a list of numbers and print only the even numbers using if.
number=[12,15,8,20,30,17,18,21,24,27,19,2,26]
# for i in number:
#     if i%2==0:
#         print("even number:",i)

# Find the sum of all numbers in a list using a loop.
number=[12,15,8,20,30,17,18,21,24,27,19,2,26]
total=0
# for i in number:
#     total=total+i

# print(total)

# Create a list of numbers and count how many numbers are greater than 10.
number=[12,15,8,20,30,17,18,21,24,27,19,2,26]
count=0
# for i in number:
#     if i>10:
#          count=count+1

# print(count)

# Create a tuple containing 5 fruits and print each fruit using a for loop.
fruit=("Banana","Mango","Grips","Apple","Orange")
# for i in fruit:
#      print(i)

# Create a tuple of numbers and check whether a given number exists in the tuple.
# n=int(input("Enter a number: "))
number=(2 ,5, 7,9,11,3,4,17,15,13,21,24,18)

# for i in number:
#     if i==n:
#         print(n,"is exists")

# Create a set of 5 numbers and print all elements using a loop.
number={5,9,14,18,21}
# for i in number:
#     print(i)
# print(type(number))

# Create a set of numbers. Check whether 10 is present in the set or not.
number={5,9,14,18,21,20,18,7,2,4,10,3,23}
# if 10 in number:
#     print(10, "present in set")

# Take a number from the user and check whether that number exists in a given list.
number={5,9,14,18,21,20,18,7,2,4,10,3,23}
# n=int(input("Enter a number: "))
# for i in number:
#     if i==n:
#         print(n,"exists in set")

# Find the largest number in a list using a loop and if condition.
number=[5,9,14,18,21,20,18,7,2,4,10,3,23]
largest=number[0]
# for i in number:
#     if i>largest:
#         largest=i
# print(largest)

# List + if + Loop -----Create a list of numbers and print: Positive numbers, Negative numbers, Ignore zero
number = [10, -5, 0, 8, -2, 15, 0, -7]
# for i in number:
#     if i>0:
#         print("Positive number",i)
#     elif i<0:
#         print("Negative number",i)

# Create a list of numbers and find how many numbers are even and how many are odd.
number=[5,9,14,18,21,20,18,7,2,4,10,3,23]
even=[0]
odd=[0]

# for i in number:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even number", even)
# print("Odd number", odd)

# Create a tuple of numbers and find the smallest number using a loop.
number=(5,9,14,18,21,20,18,7,2,4,10,3,23)
# print(type(number))

# smallest=number[0]
# for i in number:
#     if i<smallest:
#         smallest=i

# print(smallest)

# Create two sets and check whether they have any common elements.
num1={2,3,5,7,8,9,11,23,56}
num2={2,5,9,21,27,8,41,57,13}
new_set=(num1&num2)
# print(new_set)

common=set()
# for i in num1:
#     for i in num2:
#         common.add(i)
# print(common)

# Create a list of student marks. Print: --"Pass" if marks ≥ 40 , "Fail" if marks < 40
marks = [35, 45, 60, 28, 75, 39, 50]
# for i in marks:
#     if i >=40:
#         print(i,"Pass")
#     elif i<=40:
#         print(i,"Fail")

# Create a list of numbers and calculate the total and average using a loop.
number = [35, 45, 60, 28, 75, 39, 50]
# print(type(number))
total=0
# for i in number:
#     total=total+i

# print(total)

# avg=total/len(number)
# print(avg)

# Create a tuple of numbers. Find the second largest number without using sort().
number = (35, 45, 60, 28, 75, 39, 50)

