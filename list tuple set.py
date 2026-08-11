#               ----Tuple Function------

t1=(34,25,36)
# print(type(t1))

#single data ke sath tuple kaise banate hai
t1=(5,)
# print(type(t1))

#tuple packing ---ese tuple packing bolte hai
n=12,13,'ravi',34.5  #ye bhi ek tuple hai
# print(type(n))

# tuple unpacking -- ese tuple unpacking bolte hai
n=12,13,'ravi',34.5
a,b,c,d=n
# print(a,b,c,d)   # sara date 1 1 me store ho jayega
a,b ,*rest=n
# print(a,b,rest) # a=12,b=13 baki ka sara ek tuple me store ho jayega

# value swap kaise karte hai --a ka value b me or b ka value a me kaise karte hai
a,b = 1,2
a,b = b,a #value ko swap kar deta hai 
# print(a,b)

#               -------Set Function-------

# set me duplilcate value allow nhi hota autometicaly remove kar deta hai
n1={3,4,5,41,6,3,5,51,7,5,61,6,8,8,9,47,2,3,2,4} # duplicate autometic remove ho jayega
# print(n)

# new vlaue add karne ke liye
n1.add(21)
# print(n1)

# koi value remove karne ke liye
n1.remove(41)
# print(n1)

# koi value remove karne ke liye without error
n1.discard(27)
# print(n1)

# Set operation ---union, intersection & difference
a={1,2,3,4}
b={3,4,5,6}

#union sabhi value ko print karta hai
print(a|b)

#intersection --dono me common value print karta hai
print(a&b)

#difference -- a me value ho but b me nhi ho
print(a - b)

#symmetric -- dono me jo common nahi ho
print(a^b)

