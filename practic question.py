# n=int(input("enter a number"))


# Print numbers from 1 to 20 using a for loop.
# for i in range(1,21):
#     print(i)

# Print all even numbers from 1 to 50 using a while loop.
# n=1
# while n<=50:
#     if n%2==0:
#         print(n)
#     n=n+1

# Take a number from the user and print its multiplication table from 1 to 10.
# n= int(input("enter a number"))
i=1
# while i<=10:
#     print(i*n)
#     i=i+1

# for i in range(1,11):
#     print(i*n)

# Take n from the user and find the sum of numbers from 1 to n
# n= int(input("enter a number"))
# total=0
# for i in range(i,n+1):
#     total+=i
# print("sum=",total)

# Take a number from the user and find its factorial using a loop.
# n= int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact= fact*i
# print(fact)

# Take a number from the user and reverse it using a while loop.
n = 12345
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)

   