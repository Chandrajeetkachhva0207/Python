# 1. A student’s marks are entered by the user. Print the grade based on:
#90–100 → A
# 80–89 → B
# 70–79 → C
# <70 → F
#--->
# marks=int(input("Enter the marks..:"))
# if marks>=90:
#     print("A")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# else:
#     print("F")

#2. Write a program to check whether a triangle is valid or invalid. A triangle is valid if sum of all the angles is equal to 180

# angle1=int(input("age 1 is :"))
# angle2=int(input("age 2 is :"))
# angle3=int(input("age 3 is :"))

# if(angle1+angle2+angle3==180):
#     print("valid Triangle")
# else:
#     print("invalid Triangle")

#3. Check whether a number is divisible by 3 and 5 using the and operator

# number=float(input("number is :"))
# if number%3==0 and number%5==0:
#     print("divisible by 3 and 5")
# else:
#     print("not divisible..")

#4. Take a number as input and write comments explaining how your program checks if it is prime or not.
# number = int(input("Enter the number: "))

# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")
# else:
#     print("It is not a prime number")

#5. Swap two numbers  using a temporary variable

# a=5
# b=7
# temp=a
# a=b
# b=temp
# print(a)
# print(b)


#6. Swap two numbers  using a temporary variable
#method 1
# a=5
# b=7
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

#method 2

# a=5
# b=7
# a=a^b
# b=a^b
# a=a^b
# print(a)
# print(b)

#method 3
# a=5
# b=7
# a,b=b,a
# print(a)
# print(b)

# 7. Write a Python program to check whether a given shape is a square or a rectangle based on the sides entered by the user.
#Reactangle
# side1=int(input("enter the size 1.."))
# side2=int(input("enter the size 2.."))
# reactangle=2*side1+2*side2
# print(reactangle)
# #Square
# side=int(input("Enter the number.."))
# print(4*side)





