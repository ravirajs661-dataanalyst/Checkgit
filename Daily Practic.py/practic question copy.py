# # n=int(input("enter a number"))


# # Print numbers from 1 to 20 using a for loop.
# # for i in range(1,21):
# #     print(i)

# # Print all even numbers from 1 to 50 using a while loop.
# # n=1
# # while n<=50:
# #     if n%2==0:
# #         print(n)
# #     n=n+1

# # Take a number from the user and print its multiplication table from 1 to 10.
# # n= int(input("enter a number"))
# i=1
# # while i<=10:
# #     print(i*n)
# #     i=i+1

# # for i in range(1,11):
# #     print(i*n)

# # Take n from the user and find the sum of numbers from 1 to n
# # n= int(input("enter a number"))
# # total=0
# # for i in range(i,n+1):
# #     total+=i
# # print("sum=",total)

# # Take a number from the user and find its factorial using a loop.
# # n= int(input("enter a number"))
# # fact=1
# # for i in range(1,n+1):
# #     fact= fact*i
# # print(fact)

# # Take a number from the user and reverse it using a while loop.
# n = 12345
# reverse = 0

# # while n > 0:
# #     digit = n % 10
# #     reverse = reverse * 10 + digit
# #     n = n // 10
# # print(reverse)

# # n=int(input("enter a number"))
# # # for i in range(1,11):
# # #     print(n*i)

# # while i<=10:
# #     print(n*i)
# #     i=i+1

# # for i in range(1,5):
# #     for j in range(1,4):
# #         print(j)

# # Print numbers from 1 to 100. Print Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both, otherwise print the number
# # for i in range(1,51):
# #     if i%3==0  and i%5==0:
# #         print("FizzBuzz")
# #     elif i%3==0:
# #         print("Fizz")
# #     elif i%5==0:
# #         print("Buzz")
# #     else:
# #         print(i)

# # Find the sum and average of a list without using sum() or statistics.mean().Uses: Lists, Loop, Variables.
# mark=[85,75,40,31,28,38,57]
# total=0
# # for i in mark:
# #     total=total+i
# # print(total)

# # avg=total/len(mark)
# # print(avg)

# # print(sum(mark))      #1st method

# # Print numbers from 1 to 10.
# # for i in range(1,11):
# #     print(i)

# # Print numbers from 10 to 1.
# # for i in range(10,0,-1):
# #     print(i)

# i=1
# # while i<=10:
# #     print(i)
# #     i=i+1

# a=10
# # while a>=1:
# #     print(a)
# #     a=a-1

# #print all even number 1 to 50.
# n=1
# # while n<=50:
# #     if n%2==0:
# #         print(n)
# #     n=n+1

# #print all odd number 1 to 50.
# # while n<=50:
# #    print(n)
# #    n=n+2

# # Print the multiplication table of a given number.
# # n=int(input("enter a number"))
# # i=1
# # while i<=10:
# #    print(n*i)
# #    i=i+1

# # Find the sum of numbers from 1 to 100.
# i=1
# total=0
# # while i<=100:
# #     total=total+i
# #     i=i+1
# # print(total)

# # Find the sum of all even numbers from 1 to 100.
# i = 1
# total = 0
# # while i<=100:
# #     if i%2==0:
# #         total=total+i
# #     i=i+1
# # print(total)

# # Print the square of numbers from 1 to 10.
# # for i in range(1,11):
# #     print(i**2)

# # Print the cube of numbers from 1 to 10.
# # for i in range(1,11):
# #     print(i**3)

# # Print each character of a given string.
# name = "raviraj"
# i=0
# # while i <len(name):
# #     print(name[i])
# #     i=i+1

# # duplicate value kaise find kare.----Most Important Question----
# items = [1,2,2,3,4,4,4,5,9,9]
# dup=[]
# for i in items:
#     count=0
#     for j in items:
#         if i==j:
#             count=count+1
#     if count>1 and i not in dup:
#         dup.append(i)
# print(dup)

# students=("Ravi",26,"Bca",8.5)
# name, age, course, gpa=students
# print(name, age, course, gpa)

# numbers= [1,2,3,4,5,6,7]
# print(numbers)

# User se ek number lo aur check karo ki number even hai ya odd.
# n=int(input("Enter a number :"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# User se 3 numbers lo aur sabse bada number find karo.
# num=[54,75,98]
# largest=num[0]
# for i in num:
#     if i>largest:
#         largest=i
# print(largest)

# User se ek number lo aur for loop ka use karke factorial calculate karo.
# n=int(input("Enter a number: "))
# total=1
# for i in range(1,n+1):
#     total=total*i
# print(total)

# User se ek string lo aur usko reverse karo.
# text=input("enter a string :")
# print(text[::-1])

# 1.Even numbers print karo. 2.Odd numbers print karo. 3.Even numbers ka total nikalo
# numbers = [12, 5, 8, 21, 30, 7, 16]

# for i in numbers:
#     if i%2==0:
#         print("Even number :", i)

# for i in numbers:
#     if i%2!=0:
#         print("Odd number :", i)

# total=0
# for i in numbers:
#     if i%2==0:
#         total=total+i
# print("Total :", total)


# Students ki dictionary banao: Loop se har student ka result print karo: Marks >= 40 → "Pass", Marks < 40 → "Fail"
# students = {
#     "Rahul": 75,
#     "Amit": 35,
#     "Neha": 82,
#     "Ravi": 45,
#     "Priya": 28
# }

# for name, mark in students.items():
#     if mark>=40:
#         print(name, "Pass")
#     else:
#         print( name, "Fail")

# 1 se 50 tak ke numbers me se sirf woh numbers ek new list me store karo jo: 3 se divisible hain ,aur even hain.
# number=[]
# for i in range(1,51):
#     if i%2==0 and i%3==0:
#         number.append(i)

# print(number)

# Union, Intersection, Difference, symmetric Difference Find here!
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a|b) # Union
# print(a&b) #Intersecction
# print(a-b) #difference
# print(a^b) #Symmetirc

# Ek function calculate_sum() banao jo *args accept kare.
# def calculate_sum(*number):
#     total=0
#     for i in number:
#         total=total+i 
#     print(total)

# calculate_sum(10, 20, 30, 40)

# Map + Lmabda, Filter + Lambda Function --------
# numbers = [2, 5, 8, 11, 14, 17, 20]
# squre=map(lambda n: n**2, numbers)
# even_number=filter(lambda n: n%2==0, numbers)

# print(list(squre))
# print(list(even_number))

# Exception Handling. User se do numbers input lo aur division karo. Program me handle karo:
# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number :"))
#     result=a/b
# except ValueError:
#     print("Please enter a valid number!")
# except ZeroDivisionError:
#     print("Can not divide by Zero!")
# else:
#     print("Result :", result)
# finally:
#     print("program finished")

file= open("student.txt","r")
names=file.readlines()
for name in names:
    print(name.strip())
file.close()

