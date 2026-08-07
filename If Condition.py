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

age= int(input("enter your age"))
citizen_score=int(input("inter your citizen score"))
national_score=int(input("enter your national score:"))
# if age>18:
#     if citizen_score>40:
#         print("you are eligibal to vote")
#     else:
#         print("increase your score you can vote")
# else:
#     print("you are just a kid")

if age>18:
    if citizen_score>40:
        if national_score>60:
            print("you are eligible to vote")
        else:
            print("you are not eligible to vote. increase your national score")
    else:
        print("you are not eligible to vote. increase your citizen score")
else:
    if age>=16:
        print("wiat for 1-2 years")
    else:
        print("you are just a kid bro")



