import pandas as pd
import csv

# 1. Load Csv File
df=pd.read_csv(r"C:\Users\chand\Downloads\day24_Employee_Data.csv")
print("\n---row data---")#-->top records of data
print((df.head(11)))
print("\n--output--")


# print("\n---bottom 5 Rows---")#-->bottom records of data
# print((df.tail(5)))

#2.Basic Information

# print("\nShape:", df.shape)#-->it is use of define the size of data

#3. Clean text data (very important)

#clean enployee names
# df["Employee_Name"]=df["Employee_Name"].str.strip().str.title()
# print(df.head())

#clean city name
# df["City"]=df["City"].str.title().str.strip()
# print(df.head())

#clean department name
# df["Department"]=df["Department"].str.strip().str.title()
# print(df.head())

# print("\n--- cleaned text columns---")
# print(df[["employee_name","city","department"]].head())

#4.Remove Duplicates

# print("\nDuplicate Rows:",df.duplicated().sum())
# df=df.drop_duplicates()

#5.Filter Data

#employee from mumbai
# df["City"]=df["City"].str.strip().str.title()
# mumbai_emp=df[df["City"]=="Mumbai"]
# print(mumbai_emp)

#employee with salary<60000
# high_salary=df[df["Salary"]>60000]
# print(high_salary.head())

# 6.Sort Data



