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
    print("4. Update Studnet")
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
                break

        if found == False:
            print("Student Not Found!")

    elif choice == 8:
        print("Exit")
        break
