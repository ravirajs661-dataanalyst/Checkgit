
History_file="history.txt"

def show_history():
    file=open ("History.file","r")
    Lines=file.readlines()
    if len(Lines) ==0:
        print("No HIstory Found!")
    else:
        for line in reversed(Lines):
            print(line)
    file.close()

def clear_history():
    file=open("History_file","w")
    file.close()
    print("HIstory Cleared!")

def save_to_history(equcation, result):
    file=open("HIstory_file","a")
    file.write(equcation + "=" + str(result) + "\n")
    file.close()

def calcultor(user_input):
    parts=user_input.split()
    if len(parts) != 0:
        print("Invalid input! Use Formate. Number Operator Number. e.g.(8+8)")
        return

    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op == "+":
        result= num1 + num2
    elif op == "-":
        result= num1 - num2
    elif op == "*":
        result= num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You can not devide by zero!")
            return
        result= num1/num2
    else:
        print("Invalid Operator! Use only(=,-,*,/)")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("___SIMPLE CALCULATOR (Type History, clear, exit)")

    
