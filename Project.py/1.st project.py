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