import numpy as np

# marks=np.array([65,90,80,45,70,55])

#properties
"""
print(marks.ndim)
print(marks.shape)
print(marks.size)
print(marks.dtype)
"""

# Numpy Operations----
"""
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
"""
# print(marks[marks>50])

# Array Properties find this: ndim, shape, size, dtype
"""
marks=[10,20,30,40,50,60]

mark= (np.array(marks))
print(mark.ndim)
print(mark.shape)
print(mark.size)
print(mark.dtype)

"""

# Mathematical Operation Find this: Total, average, maximum, minimun
# marks=np.array([10,20,30,40,50,60])
"""
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
"""
"""
arr=np.array([10,20,30,40,50,60])
print(arr[3])
print(arr[-1])

print(arr[1:4]) #---20,30,40 print
print(arr[:4])  #first 4 elements
print(arr[3:])  #last 3 elements
"""

"""
arr=np.array([10,20,30,40,50,60,70,80])
print(arr[::2])  # har 2nd elements 
print(arr[::-1]) # reverse elements print
"""

"""f
#2D Indexing
arr=np.array([[10,20,30],
              [40,50,60],
              [70,80,90]
              ])

print(arr[2,1])  # 80 print hoga
print(arr[0,2])  # 30 print hoga

# second row print karo
print(arr[1])  

#3rd column print karo
print(arr[:,2])
"""

"""
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
# Index 2, 4 aur 6 ke elements print karo.
print(arr[2::2])

# Last 4 elements ko negative indexing/slicing ka use karke print karo.
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(arr[-4:])

# Index 0, 2, 4, 6 ke elements print karo.
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[::2])

# array se index 1, 3, 5, 7 ke elements print karo.
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[1::2])

# Array ke last 5 elements ko reverse order me print karo.
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[:-6:-1])
"""

# ----------- 2D Array------------
# arr = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# 100 ko indexing se access karo.
# print(arr[2,2])
"""
# First 2 rows kaise nikaalenge?
print(arr[:2])
print(arr[:2,2])
print(arr[:2,3])
print(arr[:3,3])
"""

# First 2 Cloumn print kare:
# print(arr[:,1])

# Array [1, 2, 3, 4, 5, 6] ko 2 rows aur 3 columns mein convert karo.
# arr=np.array([1,2,3,4,5,6])
# result=np.reshape(arr,(2,3))
# print(result)

# NumPy ka use karke 1D array banao, jisme numbers 10, 20, 30, 40, 50 hon.
# arr=([10,20,30,40,50])
# print(arr)

# Array [12, 24, 36, 48, 60] banao aur iska ndim, shape, size aur dtype print karo.
# arr=np.array([12,24,36,48,60])
# print(arr.ndim)
# print(arr.size)
# print(arr.shape)
# print(arr.dtype)

# Array [10, 20, 30, 40, 50, 60] mein se first, third aur last element access karo.
# arr=np.array([10,20,30,40,50,60])
# print(arr[::2])

# Array [5, 10, 15, 20, 25, 30, 35, 40] mein se index 2 se 5 tak ke elements nikalo. Yaad rakho, ending index include nahi hota.
# arr=np.array([5,10,15,20,25,30,35,40])
# print(arr[2:6])

# Create a 2D Array
# arr=np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])

# print(arr)
# print(arr.ndim)

# array se second row, first column ka element aur third row, second column ka element access karo.
# print(arr[2,1])
# print(arr[2,2])

# Zeros and Ones : np.zeros() aur np.ones() ka use karke 3 rows aur 4 columns ke arrays banao.
# arr1=np.zeros((3,4))
# print(arr1)
# arr2=np.ones((2,3))
# print(arr2)

# np.arange() ka use karke 10 se 50 tak ke even numbers ka array banao.
# even=np.arange(10,50,2)
# print(even)

# 1 se 12 tak numbers ka array banao aur use 3 rows aur 4 columns ke 2D array mein convert karo.
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr=arr.reshape([3,4])
# print(new_arr)

# Arrays a = [10, 20, 30] aur b = [1, 2, 3] par addition, subtraction, multiplication aur division perform karo.
# a=np.array([10,20,30])
# b=np.array([1,2,3])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Conditional Filtering : Array [12, 45, 67, 23, 89, 34, 90] mein se sirf 50 se bade numbers nikalo.
# arr=np.array([12,45,67,23,89,34,90])
# result=arr [arr > 50]
# print(result)

# Sum, Mean, Min and Max : Array [15, 25, 35, 45, 55] ka sum, average, minimum aur maximum calculate karo.
arr=np.array([15,25,35,45])

total=arr.sum(arr)
print(total)





