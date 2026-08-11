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

for i in range(5):
    n=int(input("Enter a number: "))
    numbers.append(n)

for i in numbers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

print("even number: ", even)
print("odd number: ", odd)