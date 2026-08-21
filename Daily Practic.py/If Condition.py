# f_num=int(input("enter first number"))
# s_num=int(input("enter second number"))
# add=f_num+s_num
# if add>30:
#     print("you are elegibal to voting")
# else:
#     print("ypu are not elegibal to voting")

# age>=16 and age<18 - wait for 1-2 year more.
# age<16 - you are just a kid
 
# age=int(input("enter you age"))
# if age>=18 and age<110:
#     print("Hey man! ofcourse you can vote")
# elif age>=18 and age<21:
#     print("Hello new Voter")
# elif age<16 and age<18:
#     print("you are just a kid")
# else:
#     print("Go to home")

# wap to check number is positive, negative or Zero

# num=float(input("enter the number"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("Zero")

# wap to check a number and display the even or odd

# num=int(input("enter the number :"))
# if num % 2==0:
#     print("Even Number")
# else:
#     print("Odd number")

#nestd if condition 

# age= int(input("enter your age"))
# citizen_score=int(input("inter your citizen score"))
# national_score=int(input("enter your national score:"))
# if age>18:
#     if citizen_score>40:
#         print("you are eligibal to vote")
#     else:
#         print("increase your score you can vote")
# else:
#     print("you are just a kid")

# if age>18:
#     if citizen_score>40:
#         if national_score>60:
#             print("you are eligible to vote")
#         else:
#             print("you are not eligible to vote. increase your national score")
#     else:
#         print("you are not eligible to vote. increase your citizen score")
# else:
#     if age>=16:
#         print("wiat for 1-2 years")
#     else:
#         print("you are just a kid bro")


# mark=int(input("enter your mark"))
# if mark>90:
#     print("A")
# elif mark>80:
#     print("B")
# elif mark>60:
#     print("C")
# elif mark>40:
#     print("Pramoted")
# else:
#     print("fail")

# mark=int(input("enter your mark"))
# if mark>=40:
#     print("pass")
# else:
#     print("Fail")

# same code ko ham kuchh is tarah se likh sakte hai
# print("pass" if mark>=40 else "Fail")


#match case functaiion kaise use karte hai 
# value= int(input("enter a number :"))

# match value:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case _:
#         print("invalid number")

# day= int(input("enter a day(1-7) : "))
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("invalid day")


# real life example in calculator method
num1= int(input("enter first num :"))
num2= int(input("input secind num :"))
operator= input("enter opreator (+,-,*,/) :")

match operator :
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)




