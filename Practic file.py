# # Take a number from the user and check whether it is even or odd.
# # n= int(input("Enter a number: "))
# # if n%2==0:
# #     print("even number")
# # else:
# #     print("odd number")

# # Take a number n and print numbers from 1 to n using a for loop.
# # n= int(input("Enter a number: "))
# # for i in range(1,n+1):
# #     print(i)

# # Take a number n and find the sum of numbers from 1 to n.
# # n= int(input("Enter a number: "))
# # total=0
# # for i in range(1,n+1):
# #     total=total+i
# # print(total)

# # Take a number from the user and print its multiplication table from 1 to 10.
# # n= int(input("Enter a number: "))
# # for i in range(1,11):
# #     print(n*i)

# # Take a number n and print all even numbers from 1 to n.
# # n= int(input("Enter a number: "))
# # for i in range(1,n+1):
# #     if i%2==0:
# #         print(i)

# # Create a list: Print all elements using a for loop.
# numbers=[10,20,30,40,50]
# # for i in numbers:
# #     print(i)

# # From the above list, find the sum of all elements using a loop.
# total=0
# # for i in numbers:
# #     total=total+i
# # print(total)

# # Create a list of numbers and count how many even numbers are present.
# numbers=[2,3,5,7,6,12,15,17,18,22,23,57,4,54]
# # count=0
# # for i in numbers:
# #     if i%2==0:
# #         count=count+1
# # print(count)

# # Create a list of numbers and count how many numbers are greater than 10.
# numbers = [5, 12, 8, 20, 15, 3, 25, 7]
# count=0
# # for i in numbers:
# #     if i>10:
# #         count=count+1
# # print(count)

# # Create a list:Check whether 30 is present in the list.
# numbers = [10, 20, 30, 40, 50]
# # for i in numbers:
# #     if i==30:
# #         print("30 is present")

# # Create a tuple:Print all elements using a loop.
# numbers = (10, 20, 30, 40, 50)
# # for i in numbers:
# #     print(i)

# # Find the largest number in a tuple without using max().
# largest=numbers[0]
# # for i in numbers:
# #     if i>largest:
# #         largest=i
# # print(largest)

# # Create two sets:Find their union.
# a={1,2,3,4}
# b={3,4,5,6}
# # new_set=a.union(b)
# # print(new_set)

# # Find the common elements between sets A and B.
# n = a.intersection(b)
# # print(n)

# # Given:Remove duplicate values using a set.
# numbers = [10, 20, 10, 30, 20, 40]
# # n=list(set(numbers))
# # print(n)

# # Take 5 numbers from the user, store them in a list, and print separately:
# # Even numbers
# # Odd numbers

# numbers=[]
# even=[]
# odd=[]

# # for i in range(5):
# #     n=int(input("Enter a number: "))
# #     numbers.append(n)

# # for i in numbers:
# #         if i%2==0:
# #             even.append(i)
# #         else:
# #             odd.append(i)

# # print("even number: ", even)
# # print("odd number: ", odd)

# # Create a list of 5 numbers and use a for loop to print each number.
# number=[12,15,8,20,30]
# # for i in number:
# #     print(i)

# # Create a list of numbers and print only the even numbers using if.
# number=[12,15,8,20,30,17,18,21,24,27,19,2,26]
# # for i in number:
# #     if i%2==0:
# #         print("even number:",i)

# # Find the sum of all numbers in a list using a loop.
# number=[12,15,8,20,30,17,18,21,24,27,19,2,26]
# total=0
# # for i in number:
# #     total=total+i

# # print(total)

# # Create a list of numbers and count how many numbers are greater than 10.
# number=[12,15,8,20,30,17,18,21,24,27,19,2,26]
# count=0
# # for i in number:
# #     if i>10:
# #          count=count+1

# # print(count)

# # Create a tuple containing 5 fruits and print each fruit using a for loop.
# fruit=("Banana","Mango","Grips","Apple","Orange")
# # for i in fruit:
# #      print(i)

# # Create a tuple of numbers and check whether a given number exists in the tuple.
# # n=int(input("Enter a number: "))
# number=(2 ,5, 7,9,11,3,4,17,15,13,21,24,18)

# # for i in number:
# #     if i==n:
# #         print(n,"is exists")

# # Create a set of 5 numbers and print all elements using a loop.
# number={5,9,14,18,21}
# # for i in number:
# #     print(i)
# # print(type(number))

# # Create a set of numbers. Check whether 10 is present in the set or not.
# number={5,9,14,18,21,20,18,7,2,4,10,3,23}
# # if 10 in number:
# #     print(10, "present in set")

# # Take a number from the user and check whether that number exists in a given list.
# number={5,9,14,18,21,20,18,7,2,4,10,3,23}
# # n=int(input("Enter a number: "))
# # for i in number:
# #     if i==n:
# #         print(n,"exists in set")

# # Find the largest number in a list using a loop and if condition.
# number=[5,9,14,18,21,20,18,7,2,4,10,3,23]
# largest=number[0]
# # for i in number:
# #     if i>largest:
# #         largest=i
# # print(largest)

# # List + if + Loop -----Create a list of numbers and print: Positive numbers, Negative numbers, Ignore zero
# number = [10, -5, 0, 8, -2, 15, 0, -7]
# # for i in number:
# #     if i>0:
# #         print("Positive number",i)
# #     elif i<0:
# #         print("Negative number",i)

# # Create a list of numbers and find how many numbers are even and how many are odd.
# number=[5,9,14,18,21,20,18,7,2,4,10,3,23]
# even=[0]
# odd=[0]

# # for i in number:
# #     if i%2==0:
# #         even.append(i)
# #     else:
# #         odd.append(i)

# # print("Even number", even)
# # print("Odd number", odd)

# # Create a tuple of numbers and find the smallest number using a loop.
# number=(5,9,14,18,21,20,18,7,2,4,10,3,23)
# # print(type(number))

# # smallest=number[0]
# # for i in number:
# #     if i<smallest:
# #         smallest=i

# # print(smallest)

# # Create two sets and check whether they have any common elements.
# num1={2,3,5,7,8,9,11,23,56}
# num2={2,5,9,21,27,8,41,57,13}
# new_set=(num1&num2)
# # print(new_set)

# common=set()
# # for i in num1:
# #     for i in num2:
# #         common.add(i)
# # print(common)

# # Create a list of student marks. Print: --"Pass" if marks ≥ 40 , "Fail" if marks < 40
# marks = [35, 45, 60, 28, 75, 39, 50]
# # for i in marks:
# #     if i >=40:
# #         print(i,"Pass")
# #     elif i<=40:
# #         print(i,"Fail")

# # Create a list of numbers and calculate the total and average using a loop.
# number = [35, 45, 60, 28, 75, 39, 50]
# # print(type(number))
# total=0
# # for i in number:
# #     total=total+i

# # print(total)

# # avg=total/len(number)
# # print(avg)

# # Create a tuple of numbers. Find the second largest number without using sort().
# # number = (35, 45, 60, 28, 75, 39, 50)

# User se ek number lo aur check karo positive, negative ya zero hai.
# number=int(input("Enter a number: "))
# if number>0:
#     print("positive number",number )
# elif number<0:
#     print("Negative number", number)
# else:
#     print("zero")

# User se ek number lo aur check karo even ya odd hai.
# num=int(input("Enter a number: "))
# if num%2==0:
#     print("even number", num)
# else:
#     print("odd number", num)

# 1 se 20 tak ke saare numbers print karo using for loop.
# for i in range(1,21):
#     print(i)

# 1 se 50 tak ke sirf even numbers print karo.
# for i in range(1,51):
#     if i%2==0:
#         print(i)

# 1 se 50 tak ke sirf odd numbers print karo.
# for i in range(1,51):
#     if i%2!=0:
#         print(i)

# User se n lo aur 1 se n tak ka sum find karo.
# num=int(input("Enter a number"))
# total=0
# for i in range(1,num+1):
#     total=total+i

# print(total)

# User se ek number lo aur uska factorial find karo.
# num=int(input("Enter a number"))
# total=1
# for i in range(1,num+1):
#     total=total*i

# print(total)

# User se ek number lo aur while loop se usko reverse karo.
# num=int(input("Enter a number"))
# reverse=0
# while num>0:
#     digit=num%10
#     reverse= reverse*10+digit
#     num=num//10

# print(reverse)

# User se 5 numbers ki list lo aur usme se largest number find karo.
# num=[5,9,11,3,7]
# largest=num[0]
# for i in num:
#     if i>largest:
#         largest=i

# print(largest)

# Given list mein count karo ki kitne numbers even aur kitne odd hain.
# n=[13,11,20,2,4,7,5,19,17,55,65,37,38,12,10]
# even=0
# odd=0
# count=0
# for i in n:
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1

# print("even number: ", even)
# print("odd number: ", odd)

# Duplicate values remove karo using set.
# numbers = [10, 20, 10, 30, 20, 40, 50, 30]
# num=list(set(numbers))
# print(num)

# Given list mein se sirf even numbers ka new list banao.
# numbers = [10, 20, 10,17,13, 21, 7, 30, 20, 40, 50, 30]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)

# print(even)

# Har element ko 2 se multiply karke new list banao.
# numbers = [5, 10, 15, 20, 25]
# new_l=[]
# for i in numbers:
#     new_l.append(i*2)

# print(new_l)

# Ek tuple banao aur check karo ki given element tuple mein present hai ya nahi.
# number=(2,4,10,16,17,21,7,3,9,11,27,15,13)
# print(type(number))
# n=int(input("Enter a number: "))
# if n in number:
#     print(n, "is present")
# else:
#     print(n, "is not present")

# Do sets diye gaye hain:Find: --Union, Intersection, Difference
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A|B)
# print(A&B)
# print(A-B)

# Given list mein maximum aur minimum value find karo without using max() and min().
# number=[2,4,10,16,17,21,7,3,9,11,27,15,13]
# largest=number[0]

# for i in number:
#     if i>largest:
#         largest=i
# print(largest)

# User se ek string lo aur count karo usme kitne vowels hain.
# n = str(input("Enter a Text: "))
# count=0

# for i in n:
#     if i in "aeiouAEIOU":
#         count=count+1
# print(count)

#               ----- Lambda, Map, Filter -------

# Lambda function se kisi number ka square nikalo.
# square=lambda n:n**2
# print(square(4))

# Lambda function se do numbers me se largest number find karo.
# largest= lambda a,b: a if a>b else b 
# print(largest(15,18))

# Lambda function se check karo ki number even hai ya nahi.
# check= lambda n: True if n%2==0 else False 

# print(check(6))

# Lambda function se kisi string ki length find karo.
# result=lambda n:len(n)
# print(result("RaviRaj"))

# map() + lambda ka use karke list ke har number ko double karo.
# number=[2,3,4,5,6]
# double=map(lambda n:n*2, number)
# print(list(double))

# map() ka use karke har number ka square nikalo.
# number=[2,3,4,5]
# square=map(lambda n : n**2, number)
# print(list(square))

# List ke har number me 10 add karo using map().
# number=[10,15,20,25]

# result=map(lambda n:n+10, number)
# print(list(result))

# map() + lambda se har name ko uppercase me convert karo.
# name=["raviraj","priya"]
# result=map(lambda n: n.upper(),name)
# print(list(result))

# map() + lambda se har name ko uppercase me convert karo.
# number=[1,2,3,4,5,6,7,8,9,10,11]

# even=filter(lambda n: n%2==0,number)
# print(list(even))

# List me se sirf positive numbers filter karo.
# number=[-5,10,-2,7,0,-6,9,-11,12]
# possitive=filter(lambda n: n>0,number)
# print(list(possitive))

# Sirf woh names select karo jo "A" se start hote hain.
# name=["Amit", "Rahul", "Ankit", "Rohit", "Ajay"]
# check=filter(lambda n: n.startswith("A"), name)
# print(list(check))

# User se 5 numbers input lo aur unmein se sabse bada number find karo.
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# d=int(input("Enter a number"))
# e=int(input("Enter a number"))

# largest=a 
# if b>largest:
#     largest=b 
# if c>largest:
#     largest=c 
# if d>largest: 
#     largest=d 
# if e > largest:
#     largest=e 

# print("Largest: ", largest)

# User se ek number lo aur check karo ki number even hai ya odd.
# n=int(input("Enter a number: "))
# if n%2==0:
#     print("Even No :", n)
# else:
#     print("Odd No :", n)

# User se ek number lo aur while loop ka use karke uska reverse print karo.
# num=int(input("Enter a number: "))
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10 + digit
#     num=num //10
# print(reverse)

# User se ek number lo aur uska factorial calculate karo.
# num=int(input("Enter a number: "))
# total=1
# for i in range(1,num+1):
#     total=total*i
# print(total)

# Isme se sirf even numbers ki new list banao.
# numbers=[10,15,20,25,30,35,40]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
# print(even)

# Isme vowels (a, e, i, o, u) count karo.
# text= str(input("Enter a text: "))
# count=0
# for i in text:
#     if i in "aeiouAEIOU":
#         count=count+1
# print(count)

# Duplicate values remove karke unique values print karo.
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# unique=[]
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# num1=list(set(numbers))
# print(num1)

# Ek dictionary banao jisme 5 students ke naam aur marks ho.Sirf un students ko print karo jinke marks 60 se zyada hain.
# student={
#     "Raviraj": 67,
#     "Priya": 78,
#     "Neha": 87,
#     "Namdni": 45,
#     "Amit": 55
# }
# for name, marks in student.items():
#     if marks>60:
#         print(name, marks)

# User se ek sentence lo aur dictionary ki help se har word kitni baar aaya hai count karo.
# sentence=input("Enter a sentence")
# words=sentence.split()
# count={}
# for i in words:
#     if i in count:
#         count[i]=count[i]+1
#     else:
#         count[i]=1
# print(count)

# List comprehension ka use karke 1 se 50 tak ke squares of even numbers ki list banao.
# squre=(i**2 for i in range(1,51) if i%2==0 )
# print(list(squre))

# Dictionary comprehension ka use karke 1 se 10 tak numbers aur unke squares ki dictionary banao.
# squre={n:n**2 for n in range(1,11)}
# print(squre)

# Ek function calculate(a, b, operation) banao jo operation ke according: addition, subtraction, multiplication, division 
# a=int(input("Enter a number: "))
# b=int(input("Enter a number:"))
# operation=input("Enter a operation(+,-,*,/):")

# def calculation(a,b,operation):
#     if operation =="+":
#         return(a+b)
#     elif operation=="-":
#         return(a-b)
#     elif operation=="*":
#         return(a*b)
#     elif operation=="/":
#         return(a/b)
#     else:
#         print("invalid Operator")
# result=calculation(a,b,operation)

# print("Result:", result)

# Ek function banao jo *args accept kare aur diye gaye sabhi numbers ka sum aur average return kare
# def calculation(*number):
#     total=0
#     for i in number:
#         total=total+i
#     print(total)
#     print((total)/len(number))

# calculation(12,13,24,25,16)

# Ek function banao jo **kwargs accept kare aur student ki information print kare, jaise:
# def student(**details):
#     for key, value in details.items():
#         print(key,":", value)

# student(
#     name="Raviraj",
#     age=22,
#     course="Excel, SQL, Python",
#     marks= 71.89
# )

# lambda aur map() ka use karke list ke har number ka square nikalo:
# number=[2,4,6,8,10,12,14]
# squre=map(lambda n:n**2, number)
# print(list(squre))

# lambda aur filter() ka use karke list me se 50 se greater numbers find karo:
# numbers = [25, 60, 45, 80, 30, 90, 55]
# check=filter(lambda n: n>50, numbers)
# print(list(check))

# lambda, filter() aur map() ko combine karke list me se even numbers select karo aur unka square nikalo.
# numbers = [25, 60, 45, 80, 30, 90, 55]
# even_number=filter(lambda n: n%2==0, numbers)
# squre= map(lambda n: n**2, even_number)
# print(list(squre))

# reduce() ka use karke list ke sabhi numbers ka product nikalo:
# numbers = [2, 3, 4, 5]
# from functools import reduce
# result= reduce(lambda a,b: a+b, numbers)

# print(result)

# Ek program banao jo user se number input kare. Agar user number ke instead text enter kare to try-except se error handle karo 
#                               aur "Please enter a valid number" print karo.

# try:
#     A=int(input("Enter a number :"))
#     B=int(input("Enter a number :"))
#     result=(A/B)
# except (ValueError,TypeError, ZeroDivisionError):
#     print("Please enter a valid number")
# else:
#     print("Result:", result)
# finally:
#     print("Proggram complete")

"""
 Ek student-management program banao jisme:
Student ka naam aur marks store ho
Dictionary/list ka use ho
Function ka use ho
if-else se grade calculate ho
try-except se invalid marks handle ho
lambda + filter() se 60+ marks wale students find karo
lambda + map() se students ke marks me 5 bonus marks add karo 
"""

"""
students = [
    {"name": "Rahul", "marks": 75},
    {"name": "Aman", "marks": 45},
    {"name": "Priya", "marks": 88},
    {"name": "Neha", "marks": 55},
    {"name": "Ravi", "marks": 65}
]
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Display students and grades
for student in students:
    print(student["name"], student["marks"], calculate_grade(student["marks"]))

# 60+ marks wale students
top_students = list(
    filter(lambda student: student["marks"] >= 60, students)
)

print("\n60+ Marks Students:")
print(top_students)

# 5 bonus marks add karna
bonus_students = list(
    map(lambda student: {
        "name": student["name"],
        "marks": student["marks"] + 5
    }, students)
)

print("\nAfter 5 Bonus Marks:")
print(bonus_students)

"""

# Ek function find_even(numbers) banao jo list me se even numbers return kare.
# numbers = [10, 15, 20, 25, 30, 35, 40]
# find_even=filter(lambda n:n%2==0, numbers)
# print(list(find_even))

# Ek dictionary mein 5 students ke naam aur marks store karo. Function bana kar har student ka grade print karo.
students=[
    {"Name": "RaviRaj","Mark" : 75},
    {"Name": "Priya","Mark" : 65},
    {"Name": "Neha","Mark" : 87},
    {"Name": "Nandni","Mark" : 45},
    {"Name": "Amit","Mark" : 40}
]

# def grade(mark):
#     if mark>=80:
#         return "A"
#     elif mark>=60:
#         return "B"
#     elif mark>=40:
#         return "C"
#     else:
#         return "Fail"

# for student in students:
#     result = grade(student["Mark"])
#     print(student["Name"], result)

# lambda aur filter() ka use karke list me se 50 se greater numbers find karo.
# numbers = [25, 60, 45, 80, 30, 90, 55]
# check=filter(lambda n: n>50, numbers)
# print(list(check))

# lambda aur map() ka use karke list ke har number mein 10 add karo.
# numbers = [10, 20, 30, 40, 50]
# added=map(lambda n: n+10, numbers)
# print(list(added))

# reduce() ka use karke list ke sabhi numbers ka sum nikalo.
# from functools import reduce
# numbers = [5, 10, 15, 20]
# result=reduce(lambda a,b: a+b, numbers)
# print(result)

# Is list me se sirf even numbers ki ek new list banao.
# numbers = [12, 25, 8, 41, 30, 17, 50]
# even_num=filter(lambda n: n%2!=0, numbers)
# print(list(even_num))

# 5 students ke naam aur marks ko store karo. Program aisa banao ki har student ka naam, marks aur grade print ho.
# students=[
#     {"name":"RaviRaj","mark":85},
#     {"name":"priya","mark":75},
#     {"name":"neha","mark":44},
#     {"name":"amit","mark":40},
#     {"name":"namdni","mark":55}
# ]
# def grade(mark):
#     if mark>=80:
#         return "A"
#     elif mark>=60:
#         return "B"
#     elif mark>=40:
#         return "C"
#     else:
#         return "Fail"
# for student in students:
#     result=grade(student["mark"])
#     print(student["name"],student["mark"], result)

# Is list me se 60 ya usse zyada numbers find karo aur unka square nikalo.
# numbers = [10, 25, 40, 55, 70, 85, 100]
# check=filter(lambda n: n>=60, numbers)
# square=map(lambda n: n**2, check)
# print(list(square))

# User se numbers aur operation input lena hai aur final result print karna hai.
# A=int(input("Enter a number :"))
# B=int(input("Enter a number :"))
# operation=input("Enter a operator (+,-,*,/): ")

# def calculation(A,B,operation):
#     if operation =="+":
#         return A+B
#     elif operation =="-":
#         return A-B
#     elif operation =="*":
#         return A*B
#     elif operation =="/":
#         return A/B
#     else:
#         return "Invalid operator"
# result=calculation(A,B,operation)
# print("Result :", result)

"""
Ek student-management program banao jisme:
5 students ka naam aur marks store karo.
Har student ka grade print karo.
60 ya usse zyada marks wale students alag print karo.
Sabhi students ke marks mein 5 bonus marks add karo.
Agar user invalid marks enter kare, to program crash nahi hona chahiye.

students = [
    {"name": "Rahul", "marks": 75},
    {"name": "Aman", "marks": 45},
    {"name": "Priya", "marks": 88},
    {"name": "Neha", "marks": 55},
    {"name": "Ravi", "marks": 65}
]

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

for student in students:
    print(student["name"], student["marks"], calculate_grade(student["marks"]))

top_student= list(filter(lambda student: student["marks"]>=60, students)) #---60+ wale studetnt

bonus_students=list(map(lambda student:{                    # ------5 bonus point add har student ko 
    "name": student["name"],
     "marks": student["marks"] +5
     },students))

print(top_student)
print(bonus_students)
"""


