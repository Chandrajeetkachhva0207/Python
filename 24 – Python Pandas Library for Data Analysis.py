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
#sort by Salary(Descending)
# df_sorted_salary=df.sort_values("Salary",ascending=False)
# print(df_sorted_salary.head())

#sort by joining year(Ascending)
# df_sorted_year=df.sort_values("Joining_Year")
# print(df_sorted_year.head())

# 7.Add New Columns

#Salary Category
# df["Salary_Category"]= df["Salary"].apply(
#     lambda x: "High" if x>=6000 else "Medium" if x>=50000 else "Low"
# )
# print(df.head())

# Experience(Years)
# df["Experience"]=2025-df["Joining_Year"]
# print(df.head())

#8. Group By Operations

#average Salary by department
# avg_salary_dept = df.groupby("Department")["Salary"].mean()
# print(avg_salary_dept)

#average Salary by city
# df["City"]=df["City"].str.title().str.strip()
# avg_salary_city=df.groupby("City")["Salary"].sum()
# print(avg_salary_city)

#Employee Count By Departement
# count_dept=df.groupby("Department")["Employee_ID"].count()
# print(count_dept.head())

#9.Export Cleaning Data -Sort by Salary(Descending)
df_sorted_salary = df.sort_values("Salary", ascending=False)
df_sorted_salary.to_csv("employee_sorted_by_salary.csv", index=False)


