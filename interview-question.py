# 🔹 1. What is Python?

# Answer:
# Python is a high-level, interpreted programming language used for data analysis, automation, and machine learning because it is easy to read and write.

# 🔹 2. Why is Python used in Data Analytics?

# Answer:

# Easy syntax

# Large libraries (NumPy, Pandas, Matplotlib)

# Fast data processing

# Strong community support

# 🔹 3. Difference between List and Tuple

# Answer:

# List	Tuple
# Mutable (changeable)	Immutable (not changeable)
# Uses []	Uses ()
# Slower	Faster
# lst = [1, 2, 3]
# tup = (1, 2, 3)
# 🔹 4. What are mutable and immutable data types?

# Answer:

# Mutable: List, Dictionary, Set

# Immutable: Integer, Float, String, Tuple

# 🔹 5. Difference between = and ==

# Answer:

# = assigns value

# == compares values

# a = 10
# a == 10  # True
# 🔹 6. What is type casting?

# Answer:
# Converting one data type into another.

# x = "10"
# y = int(x)
# 🔹 7. What is indentation in Python?

# Answer:
# Indentation defines code blocks. Python does not use {}.

# if x > 0:
#     print("Positive")
# 🔹 8. What is a loop?

# Answer:
# Loop repeats code multiple times.

# for i in range(3):
#     print(i)
# 🔹 9. Difference between for loop and while loop

# Answer:

# for: known number of iterations

# while: unknown number of iterations

# 🔹 10. What is a function?

# Answer:
# A reusable block of code.

# def add(a, b):
#     return a + b
# 🔹 11. What is a lambda function?

# Answer:
# One-line anonymous function.

# square = lambda x: x * x
# 🔹 12. What is list comprehension?

# Answer:
# Short way to create lists.

# squares = [x*x for x in range(5)]
# 🔹 13. How to reverse a string?

# Answer:

# s = "python"
# print(s[::-1])
# 🔹 14. Difference between append() and extend()

# Answer:

# append() adds one element

# extend() adds multiple elements

# 🔹 15. How to remove duplicates from a list?

# Answer:

# lst = [1,2,2,3]
# unique = list(set(lst))
# 🔹 16. What is dictionary?

# Answer:
# Key-value pair data structure.

# data = {"name": "Ram", "age": 22}
# 🔹 17. How to handle exceptions?

# Answer:

# try:
#     print(10/0)
# except:
#     print("Error")
# 🔹 18. What is NumPy?

# Answer:
# NumPy is a library for numerical operations and arrays.

# 🔹 19. What is Pandas?

# Answer:
# Pandas is a library for data manipulation and analysis using Series and DataFrames.

# 🔹 20. Difference between Series and DataFrame

# Answer:

# Series: 1D data

# DataFrame: 2D table

# 🔹 21. What is NaN?

# Answer:
# NaN means missing or undefined value.

# 🔹 22. How to handle missing values?

# Answer:

# fillna()

# dropna()

# 🔹 23. Difference between loc and iloc

# Answer:

# loc → label-based

# iloc → index-based

# 🔹 24. What is groupby?

# Answer:
# Used to group data and apply aggregation.

# df.groupby("dept")["salary"].mean()
# 🔹 25. Coding: Check Palindrome
# s = "madam"
# print(s == s[::-1])
# 🔹 26. Coding: Find Maximum in List
# lst = [10, 40, 20]
# print(max(lst))
# 🔹 27. Coding: Count vowels
# s = "analytics"
# count = 0
# for ch in s:
#     if ch in "aeiou":
#         count += 1
# print(count)
# 🔹 28. Coding: Fibonacci Series
# a, b = 0, 1
# for i in range(5):
#     print(a)
#     a, b = b, a+b
# 🔹 29. How to read CSV in Pandas?
# import pandas as pd
# df = pd.read_csv("data.csv")
# 🔹 30. Why Python + SQL for Data Analytics?

# Answer:

# SQL → fetch data

# Python → clean, analyze, visualize data