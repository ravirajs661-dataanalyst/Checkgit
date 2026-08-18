# Program mein error aane par program ko crash hone se bachana aur us error ko properly handle karna.

# User se do numbers input lo aur unka division karo. ZeroDivisionError ko try-except se handle karo.
# try:
#     num1=int(input("Enter a number: "))
#     num2=int(input("Enter a number: "))
#     divide=num1/num2
# except ValueError:
#     print("Please inter a valid number")
# except ZeroDivisionError:
#     print("can not divide by zero")
# else:
#     print("Result: ", divide)

# User se ek number input lo. Agar user number ki jagah text enter kare, to ValueError ko handle karke 
#                   "Please enter a valid number" print karo.

# try:
#     n=int(input("Enter a number: "))
#     print(n)
# except (ValueError,ZeroDivisionError) as e:
#     print("Error",e)

# User se index input lo aur list ka element print karo. Agar user invalid index de, to IndexError handle karo.
numbers = [10, 20, 30, 40, 50]
try:
    n=int(input("Enter a number: "))
    print(numbers[n])
except IndexError:
    print("Invlid Index! , Try Again ")


