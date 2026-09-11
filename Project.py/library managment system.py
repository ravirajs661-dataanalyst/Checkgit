from datetime import datetime 

class Student:
    def __init__(self, seat_id, name, library_name, mobile_no,addresh, parent_name, parent_mobile_no, joining_date,start_time, end_time,
                  library_fee, paid_amount):
        self.seat_id= seat_id
        self.name= name
        self.library_name= library_name
        self.mobile_no= mobile_no
        self.addresh= addresh
        self.parent_name= parent_name
        self.parent_mobile_no= parent_mobile_no
        self.joining_date= joining_date
        self.start_time= start_time
        self.end_time= end_time
        self.library_fee= library_fee
        self.paid_amount= paid_amount
        self.due_amount= library_fee - paid_amount
        self.present=True

students=[]
while True:
    print("\n=====Library Managment System=====")
    print("1. Add student")
    print("2. Show All Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Fee Details")
    print("6. Mark Student Absent")
    print("7. Delete Student")
    print("8. Exit")

    choice=int(input("Enter Your Choice: "))

    if choice == 1:
        print("Add Student")
        seat_id=input("Enter Seat_id: ")
        name= str(input("Enter Student Name: "))
        library_name=str(input("Enter your library naem: "))
        mobile_no=input("Enter Student Mobile No: ")
        addresh=input("Enter Student Addresh: ")
        parent_name=str(input("Enter Student Parent Name: "))
        parent_mobile_no=input("Enter Student Parent Mobile No: ")
        joining_date=input("Enter Student Joining Date: ")
        start_time=input("Enter Start Time: ")
        end_time=input("Enter End Time: ")
        library_fee=int(input("Enter Library Fee: "))
        paid_amount=int(input("Enter Paid Amount: "))


        student= Student(seat_id, name, library_name, mobile_no, addresh,parent_name, parent_mobile_no, joining_date, start_time, end_time,
                        library_fee, paid_amount)

        students.append(student)
        print("Student Added Successfully!")

    elif choice ==2:
        if not students:
            print("Not Data!")
        else:
            print("\n======All Students======")
            for student in students:
                print(f"Seat_id: {student.seat_id}")
                print(f"Student Name: {student.name}")
                print(f"Library Name: {student.library_name}")
                print(f"Mobile No: {student.mobile_no}")
                print(f"Addresh: {student.addresh}")
                print(f"Parent Name: {student.parent_name}")
                print(f"Parent Mobile No: {student.parent_mobile_no}")
                print(f"Student Joining Date: {student.joining_date}")
                print(f"Start time: {student.start_time}")
                print(f"End Time: {student.end_time}")
                print(f"Library Fee: {student.library_fee}")
                print(f"Paid Amount: {student.paid_amount}")
                print(f"Due Amount: {student.due_amount}")
                print(f"Student Present: {'Yes' if student.present else 'No'}")

    elif choice == 3:
        seat_id=input("Enter Seat_ID: ")
        found=False
        for student in students:
            if student.seat_id == seat_id:
                found = True
                print("\n======Student Details======")
                print(f"Seat_id: {student.seat_id}")
                print(f"Student Name: {student.name}")
                print(f"Library Name: {student.library_name}")
                print(f"Mobile No: {student.mobile_no}")
                print(f"Addresh: {student.addresh}")
                print(f"Parent Name: {student.parent_name}")
                print(f"Parent Mobile No: {student.parent_mobile_no}")
                print(f"Student Joining Date: {student.joining_date}")
                print(f"Start time: {student.start_time}")
                print(f"End Time: {student.end_time}")
                print(f"Library Fee: {student.library_fee}")
                print(f"Paid Amount: {student.paid_amount}")
                print(f"Due Amount: {student.due_amount}")
                print(f"Student Present: {'Yes' if student.present else 'No'}")            
                break
        if found == False:
            print("Student Not Found!")

    elif choice == 4:
        seat_id=input("Enter Seat Id: ")
        found=False

        for student in students:
            if student.seat_id == seat_id:
                found=True
                print("1. Update Mobile No: ")
                print("2. Update Addresh: ")
                print("3. Update Parent Mobile No: ")
                print("4. Update Start Time: ")
                print("5. Update End TIme: ")
                print("6. Update Fee: ")

                update_choice=int(input("Enter Your Choice: "))
                if update_choice == 1:
                    student.mobile_no= input("Enter New Mobile No: ")
                    print("Successfully Updated!")
                elif update_choice == 2:
                    student.addresh=input("Enter New Addresh: ")
                    print("Successfully Updated!")
                elif update_choice == 3:
                    student.parent_mobile_no=input("Enter Mobile No: ")
                    print("Successfully Updated!")
                elif update_choice == 4:
                    student.start_time=input("Enter Start Time: ")
                    print("Successfully Updated!")
                elif update_choice == 5:
                    student.end_time=input("Enter End Time: ")
                    print("Successfully Updated!")
                elif update_choice == 6:
                    student.library_fee=int(input("Enter Library Fee: "))
                    student.due_amount=student.library_fee - student.paid_amount
                    print("Fee Update Successfully!")
                else:
                    print("Invalid Input!")

    elif choice == 5:
        seat_id=input("Enter Seat Id: ")
        found=False
        for student in students:
            if student.seat_id ==seat_id:
                found==True
                print(f"Seat Id: {student.seat_id}")
                print(f"Library Fee: {student.library_fee}")
                print(f"Paid Amount: {student.paid_amount}")
                print(f"Due Amount: {student.due_amount}")
                break
        if found == False:
            print("Student Not Found!")

    elif choice == 6:
        seat_id= input("Enter Seat Id: ")
        found=False
        for student in students:
            if student.seat_id==seat_id:
                found=True
                present=input("Student Present (Yes/No)")
                if present.lower =="no":
                    students.remove(student)
                    print("Student Record Delete!")
                else:
                    student.present=True
                    print("Student Still Present!")
                break
        if not found:
            print("Student Not Found!")

    elif choice == 7:
        seat_id = input("Enter Seat Id: ")
        found = False
        for student in students:
            if student.seat_id==seat_id:
                found=True
                confirm=input("Are You Sure Delete Student(Yes/No)")
                if confirm.lower =="yes":
                    students.remove(student)
                    print("Delete Student Record! ")
                else:
                   print("Delete Cancelled!")
                break
        if not found:
            print("Student Not Found!")

    elif choice == 8:
        print("Exit")
        break
