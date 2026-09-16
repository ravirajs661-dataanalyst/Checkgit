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
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

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
print(arr[:,1])




