
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






    