a=['Ravi',26, True,71.8,67]
# print(a)

#list ka length kaise find kare
# l=len(a)
# # print(l)

#list ko loop me kaise use karte hai --1st method
l=len(a)
# for i in range(0,l):
#     print(a[i])

#list ko loop me kaise use karte hai --2nd method
a=['Ravi',26, True,71.8,67]
# for i in a:
#     print(i)

#string slicing -- print(start:end:step)
a=['Ravi',26, True,71.8,67]

# # print(a)
# print(a[:4])
# print(a[2:5])
# print(a[::2])

# list ko reverse me kaise print kare 
a=['Ravi',26, True,71.8,67]
# print(a[::-1])   --#1st method
# rev_a=a[::-1]
# print(rev_a)     --#2nd method

list=[10,5,17,19,7,20,13]
# list me koi new num. add karne ke liye --.append last me value add karta hai
# list.append(20)
# print(list)
# list.append(21)
# print(list)

# .insert() insert index ke place par value ko add karta hai
# list.insert(2,3)
# print(list)

# list me koi value ko remove karne ke liye --.remove me jo value diya jatega us value ko remove kar dega. (first matching value remove karta hai)
# list.remove(13)
# print(list)

# .pop last value remove karta hai -- list se jo value remove karega use print bhi karta hai taki pata chale ko kaon si value remove ho gyi
# a=list.pop()
# print(a)

#list me kisi value ko replace karna ho to --5 ke jagah par 9 karna ho to index dena padta hai
list=[10,5,17,19,7,20,13]
list[1]=9
print(list)