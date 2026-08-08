# loop 1.for 2.while

# for i in range (1,6,1):
#     print("Hello world")

# for i in range (2,21,2):
#     print(i)

# for r in range(1,11):
#     print("Ravi Raj")


#break loop:
    #(i==3 hone par pura loop break ho jata hai)
# for i in range (1,6):
#     if i==3:
#         break
#     print(i)

#continue loop:
    #(i==3 hone par 3 ko skip kar deta hai or aage badh jata hai)
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)

#while loop: (jab tak condition true rahega tak loop chalta rahega)
# i=1
# while i<=10:
#     print("Ravi Raj")
#     i=i+1

# continue look in while(i==3 i ka value 3 hone par niche ka koi bhi line print nhi hoga)
# while i<=5:
#     if i==3:
#         continue
#     print(i)
#     i=i+1

#break loop in while(i==4 i ka vlaue 4 hone par pura loop terminate ho jata hai)
# while i<=5:
#     if i==4:
#         break
#     print(i)
#     i=i+1

# while with else(jab tak condition true hoga tab print i hoga jab condition false hoga tak else print hoga )
# while i<=5:
#     print(i)
#     i=i+1
# else:
#     print("end off loop")

# Note: while and For dono ke sathh else use hota hai 

# wap to display the table of n upto 10
# n=int(input("enter a number"))
# for i in range(1,11):
#     print(n*i)

#wap to display the table of n upto 10
# n=int(input("enter a number"))
# i=1
# while i<=10:
#     print(n*i)
#     i=i+1

# print the sum of numbers from 1 to 100 to using a loop 
i = 1
sum = 0

while i <= 100:
    sum = sum + i
    i = i + 1

print("Sum =", sum)