import numpy as np

# print("--creating a array--")
# arr=np.array([10,20,30,40,50,60,70])
# print(arr)

# print("--indexing and slicing--")
# print(arr[1])
# print(arr[0:4])

# print("--vectorized operartion--")
# print(arr+10)
# print(arr*2)
# print(arr**2)

# print("--numpy function--")
# print(arr.sum())
# print(arr.mean())
# print(arr.max(),arr.min())

# print("--data cleaning example--")
# data=np.array([20,30,40,-40,15,10,15])
# clean=data[data>=15]
# clean_unique=np.unique(clean) #that the you want the unique values .unique function use
# print(clean_unique)

# marks=np.array([80,90,-1,75,-1,60])
# marks[marks==-1]=marks[marks!=-1].mean() #replacing average of non negative value
# print("filled missing",marks


# cities=np.array(["mumbai","Pune","DelHi","MuMbai"])
# cities=np.char.strip(cities),
# cities=np.char.title(cities)
# print(cities)

#------------->practice question<-------------
# Creating NumPy Arrays : Create 1D Array
# arr=np.array([10,20,30,40,50,60,70,80,90,100])
# print(arr)

# Create 2D Array
# arr2=np.array([[10,20],[30,40]])
# print(arr2)

# Create Array with Range
# arr=np.arange(1,21)
# print(arr)

#Array with Fixed Values
#zeros = np.zeros(5)
#ones = np.ones(5)
# print(arr)

#Random Array
# rand = np.random.randint(10, 100, 5)
# print(rand)

#Array Indexing
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])
# print(arr[:-1])
# print(arr[1:3])
# print(arr[:3])
# print(arr[4:])

#Addition
arr=np.array([10,20,30,40])
# print(arr+10)

#multiple
# print(arr*2)

#Square of all items
# print(arr**2)

#Sum, Mean, Min, Max
# print(arr.sum())
# print(arr.mean())
# print(arr.min(),arr.max())

# Standard Deviation
# print(arr.std())

#Reshape Array
# arr = np.arange(1, 10)
# print(arr.reshape(3,3))

#Real Data Cleaning Examples

#remove negative value
# arr=np.array([10,-20,30,-40,50])
# clean=arr[arr>=0]
# print(clean)


# data=np.array([10,20,-30,-40,50,60])
# clean=data[data>=0]
# print(clean)


#replacing the values
# marks=np.array([80,90,-1,75,-1,60])
# marks[marks==-1]=marks[marks!=-1].mean()
# print(marks)

#Example 3 – Filter Values > 20

# arr=np.array([10, 25, 30, 5, 50])
# filtered=arr[arr>20]
# print(filtered)

#Example 4 – Multiply All Prices by Qty (Vectorized Calculation)
# Qual=np.array([2,4,5,6])
# price=np.array([20,10,25,10])
# total=Qual*price
# print(total)

