#26 – AI-Enabled Python for Data Analysis

import pandas as pd
from datetime import datetime

# Load CSV file
df = pd.read_csv("employee_sorted_by_salary.csv")

# 1. Clean names and cities
df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Add Experience column
# current_year = datetime.now().year
# df["Experience"] = current_year - df["Joining_Year"]

# Display result
print(df)

#  Optional: Save cleaned file
# df.to_csv("cleaned_employee_data.csv", index=False)
