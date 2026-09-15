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

"""
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

