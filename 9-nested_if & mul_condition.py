# print("check your eligibility")

# age=(int(input("Entar the age")))
# if  age>=18:
#     password=int(input("Enter the password"))
#     if password == 123:
#         print("password Succesfull....")
#     else:
#         print("worng password")   
# else :
#     print("you are underage")

# Multiple conditions (and)
# age=int(input("Enter your age :"))
# residence=input("Are you Indian? : ")

# if age>=18 and residence.lower()=="yes":
#     print("Eligible to drive")
# else:
#     print("Not Eligible to drive")



# Multiple conditions (OR)
age=int(input("Enter your age :"))
residence=input("do you have licence : ")

if age>=18 or residence.lower()=="yes":
    print("Eligible to register")
else:
    print("Not Eligible to register")