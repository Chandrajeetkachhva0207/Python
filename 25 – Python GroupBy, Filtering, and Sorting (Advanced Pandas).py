#25 – Python GroupBy, Filtering, and Sorting (Advanced Pandas)

import pandas as pd

#load cleaned employee data
df = pd.read_csv(r"C:\Users\chand\Downloads\day24_Employee_Data.csv")
print("\n-- Data Loaded---")
print(df.head())

#Filtering

#Employees from Mumbai
# df["City"]=df["City"].str.strip().str.title()
# mumbai_emp=df[df["City"]=="Mumbai"]
# print(mumbai_emp)

#High Salary employee
# high_salary=df[df["Salary"]>60000]
# print(high_salary)

#Multiple Condition
# mumbai_high=df[(df["City"]=="Mumbai") & (df["Salary"]>60000)]
# print(mumbai_high)

# mumbai_pune_high = df[((df["City"] == "Mumbai") | (df["City"] == "Pune")) & (df["Salary"] > 60000)]
# print(mumbai_pune_high)

#Using isin()
# IT_and_Finance=df[df["Department"].isin(["IT","Finance"])]
# print(IT_and_Finance)


#Advance Sorting

#sort by Salary Descending
# df_sorted_salary = df.sort_values("Salary", ascending=False)

#Sort by Department then Salary
# df_sorted_multi=df.sort_values(["Department","Salary"],ascending=[True,False])
# print(df_sorted_multi)

#GROUP BY OPERATIONS

#Average salary by department
avg_salary_dept = df.groupby("Department")["Salary"].mean()
# print(avg_salary_dept)

#Total salary by city
# total_salary_city = df.groupby("City")["Salary"].sum()

#Employee count by department
# emp_count_dept = df.groupby("Department")["Employee_ID"].count()

#Multiple aggregations
salary_stats = df.groupby("Department")["Salary"].agg(["min", "max", "mean", "count"])
print(salary_stats)

# SORT GROUPBY RESULT
sorted_avg_salary = avg_salary_dept.sort_values(ascending=False)
print("\nDepartments by Avg Salary:")
print(sorted_avg_salary)

