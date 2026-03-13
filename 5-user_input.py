#Input and Type-casting

# name=input("enter the user name")
# age=input("enter the age")
# roll_no=input("enter the roll number")

# print("welcome ",name)
# print("your age is",age)
# print("your roll_number",roll_no)

#Type Casting
  
#type Casting int

# age=int(input("enter the age")) 
# age=age+5
# print(age)

#type Casting float

# temp=float(input("enter the temp"))
# temp+=56
# print(temp)

#type Casting string
# amount=50000
# text="total sale :" + str(amount)
# print(text)

#total sell cacluated

# product_name=(input("entar the product name"))
# product_quantity=int(input("enter the product quantity"))
# product_per_unit=int(input("product per unity"))

# total_sell=(product_per_unit * product_quantity)

# print(product_name)
# print(total_sell)
 

#create the calculator 

# fnum=int(input("enter the first number :"))
# snum=int(input("enater the second number :"))

# addition_num=fnum+snum
# subctrated_num=fnum-snum
# multi_num=fnum*snum
# div_num=fnum/snum

# print(addition_num)
# print(subctrated_num)
# print(multi_num)
# print(div_num)

# Assignment :1) salary slip calculator

# Employee_Name=input("Enter the Employee_name :")
# Basic_Salary=float(input("Enter the Basic Salary :"))
# Bonus_Amount=float(input(" Enter the Bonus Amount :"))
# Tax_Percentage=float(input("Enter the Tax Percentage :"))

# Gross_Salary = Basic_Salary + Bonus_Amount
# Tax_Amount = Gross_Salary * Tax_Percentage / 100
# Net_Salary = Gross_Salary - Tax_Amount

# print ("======Finally, print a clean and clear Salary Slip showing all the values.=======")
# print(Employee_Name)
# print(Gross_Salary)
# print(Tax_Amount)
# print(Net_Salary)

# Assignment :2)Discount Price Calculator

# item_name=input("Enter the item_name :")
# price=float(input("Enter the price:"))
# discount_percentage=int(input("discount percentage:"))
# discount=price * discount_percentage/100 
# final_price=price-discount

# print(item_name)
# print(discount_percentage)
# print(discount)
# print(final_price)

# Assignment :3)Student Marks Percentage

student = input("Enter Student Name: ")
marks_obtained = float(input("Marks Obtained: "))
total_marks = float(input("Total Marks: "))
percentage = (marks_obtained / total_marks) * 100
print(student, "scored", percentage, "%")