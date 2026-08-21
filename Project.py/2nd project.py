import random
import string

passwords={}

try:
    with open("passwords.txt","r") as file:
        for line in file:
            website,password= line.strip.split(":")
            passwords[website]=password 
except:
    pass

def generate_password():
    chars=string.ascii_letters + string.digits + "@!#$^&*"
    password="".join(random.choice(chars) for _ in range(8))
    return password
while True:
    print("\n-----Persional password manager-----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    Choice=input("Enter your Choice :")

    if Choice == "1":
        Website=input("Enter your website :")
        Password=input("Enter your Password :")
        passwords[Website]=Password

        with open("passwords.txt","a") as file:
            file.write(f"{Website}:{Password}\n")
        print("Saved!")

    elif Choice == "2":
        if not passwords:
            print("No data!")
        else:
            for Website, Password in passwords.items():
                print(Website,":", Password)
    elif Choice == "3":
        print("generate password",generate_password())
    elif Choice == "4":
        print("Good by...")
        break
    else:
        print("Invalid input")

        


