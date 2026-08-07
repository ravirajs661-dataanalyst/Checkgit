# f_num=int(input("enter first number"))
# s_num=int(input("enter second number"))
# add=f_num+s_num
# if add>30:
#     print("you are elegibal to voting")
# else:
#     print("ypu are not elegibal to voting")

# age>=16 and age<18 - wait for 1-2 year more.
# age<16 - you are just a kid
 
age=int(input("enter you age"))
if age>=18 and age<110:
    print("Hey man! ofcourse you can vote")
elif age>=18 and age<21:
    print("Hello new Voter")
elif age<16 and age<18:
    print("you are just a kid")
else:
    print("Go to home")


