# def intro(name,age,prof):
#     print(name, age, prof)

# # intro("Raviraj",22,"Data analyst")

# def add(a,b):
#     print("sum is", (a+b))

# add(10,20)
# add(30,40)
# add(145,809)

# check karna hai "Pass" and "Fail"
# def check_result(mark):
#     if mark>=40:
#         print("Pass")
#     else:
#         print("Fail")

# check_result(75)
# check_result(22)

# Square nikalna ho to 
# def square(n):
#     return(n*n)

# print(square(5))ff

# Multipale values ko kaise return karen        ----- Important Question --------
# def calculation(a,b):
#     total=a+b
#     difference= a-b
#     return total, difference

# total, difference = calculation(10,5)

# print("Total:", total)
# print("Difference:", difference)

# def employee(name, salary):
#     annual_salary= salary*12
#     return name, salary, annual_salary

# name,salary,annual_salary = employee("Ravi",30000)

# print(name)
# print(salary)
# print(annual_salary)

# List se value find karna ------

# list=[20,30,27,10,17,35]

# def calculation(number):
#     total=sum(number)
#     return total

# result=calculation(list)

# print(result)

#  List se multiple value kaise find karen
# list=[20,30,27,10,17,35]

# def calculation(number):
#     total=sum(number)
#     max_v=max(number)
#     min_v= min(number)
#     return total, max_v, min_v

# total, max_v, min_v = calculation(list)

# print(total)    #total value find karna  
# print(max_v)    #max value find karna
# print(min_v)    #min value find karna

#  First and Last value ko find kaise kare
list=[20,30,27,10,17,35]

def get_values(number):
    first=number[0]
    last=number[-1]
    return first, last

first, last= get_values(list)

print(first)
print(last)