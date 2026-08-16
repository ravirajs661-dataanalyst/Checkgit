#  *args ka use function mein multiple positional arguments lene ke liye hota hai.

# def add(*args):
#     print(args)

# add(10,20,30)

# Real life example in *args
# def add(*number):
#     total = 0
#     for i in number:
#         total=total+i
#     print(total)

# add(10, 20, 14, 25, 26, 48)
# add(10, 20 ,14,25,26,48)

# Create a function square() that takes a number and returns its square.
# def square(n):
#     return(n*n)

# # print(square(5))

# Create a function add() that takes two numbers and returns their sum.
# n1=int(input("Enter a number"))
# n2=int(input("Enter a number"))

# def add(n1,n2):
#     print(n1 + n2)

# add(n1,n2)

# Create a function sum_numbers(*args) that accepts any number of numbers and returns their total.
# def sum_numbers(*number):
#     total=0
#     for i in number:
#         total=total+i
#     print(total)

# sum_numbers(12,37,84,92)

# Create a function find_max(*args) that accepts any number of numbers and finds the maximum number.
# def find_max(*number):
#     return max(number)

# max=find_max(34,85,98,109)
# print(max)

# Create a function count_numbers(*args) that counts how many numbers were passed.
# def count_numbers(*number):
#     count=0
#     for i in number:
#         count=count+1
#     print(count)

# count_numbers(10, 20, 30, 40)

# Create a function even_numbers(*args) that accepts multiple numbers and prints only the even numbers.
# def even_numbers(*numbers):
#     for i in numbers:
#         if i%2==0:
#             print(i)

# even_numbers(10, 15, 20, 25, 30)

# Create a function average(*args) that accepts any number of numbers and calculates their average.
# def average(*numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     print((total)/len(numbers))

# average(10, 20, 30, 40)

# Create a function student(**kwargs) that accepts student information and prints all the details.
# def student(**kwargs):
#     print(kwargs)

# student(name="Ravi", age=26, city="Patna")

# Create a function employee(**kwargs) that prints the employee's name and salary.
# def employees(**employee):
#     name=employee.get("name")
#     salary=employee.get("salary",25000)
#     print(name,salary)

# employees(name="Ravi")

# Create a function product(**kwargs) that uses these default values:
# def product(**kwargs):
#     name=kwargs.get("name","unknown")
#     price=kwargs.get("price",0)
#     quantity=kwargs.get("quantity",1)
#     print(name, price, quantity)

# product(name="Laptop", price="50000")

# def student(*subject, **details):
#     print("subject",subject)
#     print("details",details)

# student(
#     "python",
#     "sql",
#     "Excel",
#     name="Ravi",
#     city="Patna"
# )

# Create a function shopping(*items, **customer). It should print:All shopping items, Customer name,Customer city
# def shopping(*items, **customer):
#     print("items",items)
#     print("customer",customer)

# shopping(
#     "laptop",
#     "keybord",
#     "Mouse",
#     name="Ravi",
#     city="Patna"
# )

# Create a function calculate(*numbers, **options).
# def calculation(*number,**options):
#     operation =options.get("operation","sum")
#     if operation=="sum":
#         print(sum(number))
#     elif operation=="max":
#         print(max(number))
#     else:
#         print("invalid operation")

# calculation(10,20,30,operation="max")

# Create a function that accepts any number of numbers using *args and returns their total.
# def calculation(*number):
#     total=0
#     for i in number:
#         total=total+i
#     print(total)

# calculation(13,25,15,38)

# Create a function using *args that finds and returns the largest number.
# def max_number(*number):
#     print(max(number))

# max_number(45,86,84,74)

# Create a function using **kwargs that prints all student details passed as keyword arguments.
# def students(**details):
#     name=details.get("name")
#     city=details.get("city")
#     course=details.get("course")

#     print(f'name="{name}"')
#     print(f'city="{city}"')
#     print(f'course="{course}"')

# students(
#     name="RaviRaj", 
#     city="patna", 
#     course="Python, SQL, Excel"
# )

# Create a function that accepts multiple numbers using *args and student information using **kwargs.
def students(*subject,**details):
    print("subject", subject)
    print("details",details)

students(
    "Python", 
    "Sql" 
    "Excel",
    name="Raviraj",
    city="patna",
    profession="Data Analyst"
)

# *args + **kwargs – Order Details
def order(*prices,**customer):
    total=sum(prices)
    print("Total_price:",total)
    print("customer information:",)
    for key, value in customer.items():
        print(f'{key}="{value}"')

order(
    500,300,200,
    name="Raviraj",
    city="patna",
    Mobille=7079399892
)