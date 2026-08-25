"""
Student={}

while True:
    print("\n-----Student Manager Report-----")
    print("1. Add Student")
    print("2.View Student")
    print("3. Check Result")
    print("4. Exit")

    Choice=input("Enter your Choice :")

    if Choice=="1":
        Name=input("Enter student name :")
        Marks=int(input("Enter student mark :"))
        Student[Name]=Marks
        print(f"{Name} successfullu added!")

    elif Choice=="2":
        if not Student:
            print("student not found!")
        else:
            for Name,Marks in Student.items():
                print(Name,Marks)
    elif Choice=="3":
        Name=input("Enter student name :")
        if Name in Student:
            Marks=Student[Name]
            if Marks>=40:
                print("pass")
            else:
                print("Fail")
    elif Choice=='4':
        print("exiting....")
        break 
    else:
        print("Inalid input!")
"""

# Student={}

# while True:
#     print("\n-----Student Manager Report-----")
#     print("1. Add Student")
#     print("2. View Students")
#     print("3. check Result")
#     print("4. Exit")

#     choice=input("Enter Your Choice :")

#     if choice == "1":
#         Name= input("Enter Student Name :")
#         while True:
#             mark=int(input("Enter student Mark (0-100):"))
#             if 0<= mark <=100:
#                 break
#             else:
#                 print("Invalid Marks! please enter marks between 0 to 100")
#         Student[Name]=mark

#     elif choice == "2":
#         if not Student:
#             print("student not found!")
#         else:
#             for Name, mark in Student.items():
#                 print(Name, mark)

#     elif choice == "3":
#         Name=input("Enter Student name :")
#         if Name in Student:
#             mark=Student[Name]
#             if mark >=40:
#                 print("Pass")
#             else:
#                 print("Fail")

#     elif choice == "4":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid input!")

