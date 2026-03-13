# print("Enter the information of student")

# Student_name="kartik Memane"
# Student_Designation="sql developer"
# Student_eduction="BE Computer"
# Student_salary=45000

# print("Student name is",Student_name)
# print("Student Designation is",Student_Designation) 
# print("Student education is",Student_eduction)
# print("Student salary is",Student_salary)

#String
# customer_name="chandrajeet"
# print("customer name is :",customer_name)
# print("datatype name",type(customer_name))

# #2 Numerical datatype
# #int,float,complex
# customer_name=1
# customer_salary=34500.0
# a=3+4j
# print(customer_name)
# print(customer_salary)
# print(a,type(a))

#3 Boolean type
# student_result="true" 
# print(student_result,type(student_result))

# #4 sequence type
# #list,
# colleges=["ssbt","kbc num","smt,kkwagh"]
# print(colleges)
# print(type(colleges))

# cities=["jalgaon","mumbai","nashik","dhule"]
# print(cities)
# print(type(cities))

#tuples
# marks=(53,65,78,98,45,34)
# print(marks)
# print(type(marks))

# numbers=(46,73,12,34,56,78)
# print(numbers)
# print(type(numbers))

#range
# num=range(5)
# print(list(num))
# print(type(num))    

# num=range(26)
# print(list(num))

#5 dictionary type
# Teacher={
#     "teacher_id":207,
#     "teacher_name":"chandrajeet",
#     "teacher_subject":"python"
# }
# print(Teacher)
# print(type(Teacher))

#6 set type
# numbers={23,45,46,76,89}
# print(numbers)
# print(type(numbers))

# name={"chandrajeet","kartik","satyarth","kartik"}
# print(name)
# print(type(name))

# Arithamatic Operators
# a=10
# b=5

# print("Addition of a and b is:",a+b)
# print("Subtraction of a and b is:",a-b)
# print("Multiplication of a and b is:",a*b)
# print("Division of a and b is:",a/b)
# print("Modulus of a and b is:",a%b)
# print("Power of a and b is:",a**b)

#assigment Operator

# value=31
# a=10
# a=+value+a
# print(a)

# num=10

# num+=5
# print(num)

# num=-5
# print(num)

# num*=5
# print(num)

# num/=5
# print(num)

# num%=5
# print(num)

#Input and Type-casting
# stud_name=input("enter the student name")
# stud_designation=input("enter the student designation")
# stud_education=input("enter the student education")

# print("student name is",stud_name)
# print("student designation is",stud_designation)        
# print("student education is",stud_education)

#Type Casting
  
#type Casting int

# age=int(input("enter the age of student"))
# age=age+5
# print(age) 

#type Casting float

# temp=float(input("enter the temp")) 
# temp=temp+10
# print(temp)

#type Casting string
# amount=50000
# text ="total sale:"+str(amount)
# print(text)

# amounts=10000
# text="total sale:"+str(amounts)
# print(text)

#total sell cacluated

# product_name=(input(("enter the product_name")))
# product_quanitity=int(input("enter the product quantity"))
# product_price=int(input("enter the product price"))

# total_sell=(product_quanitity*product_price)
# print(product_name)
# print(total_sell)

#create the calculator 

# f_num=int(input("enter the frist number :"))
# s_num=int(input("enter the second number :"))

# addition_num=f_num+s_num
# subtraction_num=f_num-s_num
# multiplication_num=f_num*s_num
# division_num=f_num/s_num
# print("addition of two number is :",addition_num)
# print("subtraction of two number is :",subtraction_num)                 
# print("multiplication of two number is :",multiplication_num)
# print("division of two number is :",division_num)

# Assignment :1) salary slip calculator

# Employee_name=input("enter the employee name :")
# Basic_Salary=float(input("enter the basic salary : "))
# HRA=(Basic_Salary*10)/100
# DA=(Basic_Salary*5)/100
# Gross_Salary=Basic_Salary+HRA+DA                    
# print("Employee name is :",Employee_name)
# print("Basic Salary is :",Basic_Salary)
# print("HRA is :",HRA)
# print("DA is :",DA)
# print("Gross Salary is :",Gross_Salary)

# Student Marks Percentage
# strudent_name=input("enter the nameof student :")
# total_marks=int(input("enter the total marks :"))
# obrtain_marks=int(input("entar the obrtain marks :"))

# percentage=(obrtain_marks/total_marks)*100
# print("student name is:",strudent_name,"percentage is:",percentage)

#String Indexing

# string="chandrajeet"
# print(string)
# print(string[0])
# print(string[5])

#String Slicing
# product_name="notebook"
# print(product_name[0:5])
# print(product_name[::-1])

#Practical Use Cases Of Slicing
# product_name="laptop-pro-2024"
# print(product_name[-4:])

# student_name="chandrajeet kachhva"
# print(student_name[0:11])

# reverse_string="i am king of the ring"
# print(reverse_string[::-1])

#STRING METHODS (VERY IMPORTANT)

# text1="    hello python learners     "
# print(text1)

# #Remove Spaces
# print(text1.strip())

# #Convert to capital letter
# print(text1.upper().strip())

# #Convert into Proper Case
# print(text1.title().strip())

# #Convert into Lower Case
# print(text1.lower().strip())

# #Replace Word
# print(text1.replace("hello python learners ","chandrajeet kachhva").strip())

# #Count occurrences of a letter of word
# print(text1.count("h"))

# #Check if text start with something
# print(text1.strip().startswith("hello python learners"))

# #check if only numbers are present int data
# phone_number="988849459"
# print(phone_number.isnumeric())

# #Split string into list of words
# call="welcome to chandrajeet kachhva"
# words=call.split()
# print(words)

# massage="book name is wings of fire"
# rajput=massage.split()
# print(rajput)

# proffsional="i beacome the data anltytics"
# job=proffsional.split()
# print(job)

# #join back with hypen
# joined_text="-".join(words)
# print("join text:",joined_text)

# joined_text1="-".join(rajput)
# print("join text:",joined_text1)

# joined_text2="-".join(rajput)
# print("join text:",joined_text2)

# #find the position of letter
# print(massage.find("w"))

# #Extract Domain
# email="chandrajeetkachhva@gmail.com"
# domain=email[email.find("@")+1:]
# print("Domain :"+domain)


# student_name="    chandrajeet kachhva   "
# print(student_name.strip())

# #Convert to capital letter
# print(student_name.upper().strip())
# #Convert into Proper Case
# print(student_name.title().strip())
# #Convert into Lower Case
# print(student_name.lower().strip())
# #Replace Word
# print(student_name.replace("chandrajeet kachhva","kartik memane").strip())
# #Count occurrences of a letter of word
# print(student_name.count("a"))
# #Check if text start with something     
# print(student_name.strip().startswith("chandrajeet kachhva"))

#problem of if-else

#age problem

# age = int(input("Check your eligibility: "))

# if age >= 18:
#     print("Age is right")

#     password = int(input("Enter the password: "))
#     if password == 123:
#         print("Right password")
#     else:
#         print("Wrong password")

# else:
#     print("Not eligible")

# age=int(input("Enter the age.."))
# vote=int(input("enter the voter age..."))

# if(age>=18)and(vote>=18):
#     print("vote..")
# else:
#     print("not vote..")

#     age=int(input("Enter your age :"))
# residence=input("do you have licence : ")

# if age>=18 or residence.lower()=="yes":
#     print("Eligible to register")
# else:
#     print("Not Eligible to register")



#------------------------------->loop question<------------------------------------------------------

