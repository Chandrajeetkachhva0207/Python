#27 – AI-Generated Pipeline Automation Using Python

import pandas as pd

# Load data
df = pd.read_csv(r"C:\Users\chand\Downloads\raw_sales_data.csv")

# -----------------------------
# 1. Clean text columns
# -----------------------------
df["Customer_Name"] = df["Customer_Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["State"] = df["State"].str.strip().str.title()

# -----------------------------
# 2. Remove duplicate orders
# -----------------------------
df = df.drop_duplicates(subset="Order_ID")

# -----------------------------
# 3. Convert numeric columns
# -----------------------------
numeric_cols = ["Quantity", "Unit_Price", "Discount"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing numeric values (optional)
df[numeric_cols] = df[numeric_cols].fillna(0)

# -----------------------------
# 4. Calculate Total Sales
# -----------------------------
df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]) - df["Discount"]

# -----------------------------
# 5. Categorize order value
# -----------------------------
def categorize_sales(value):
    if value >= 10000:
        return "High"
    elif value >= 5000:
        return "Medium"
    else:
        return "Low"

df["Order_Value_Category"] = df["Total_Sales"].apply(categorize_sales)

# -----------------------------
# 6. Summary Reports
# -----------------------------

# Total sales by City
city_summary = df.groupby("City")["Total_Sales"].sum().reset_index()

# Total sales by Product Category
category_summary = df.groupby("Product_Category")["Total_Sales"].sum().reset_index()

# -----------------------------
# 7. Sort summaries (Descending)
# -----------------------------
city_summary = city_summary.sort_values(by="Total_Sales", ascending=False)
category_summary = category_summary.sort_values(by="Total_Sales", ascending=False)

# -----------------------------
# 8. Export to CSV
# -----------------------------
df.to_csv("cleaned_sales_data.csv", index=False)
city_summary.to_csv("sales_by_city.csv", index=False)
category_summary.to_csv("sales_by_category.csv", index=False)

# Display outputs
print("Cleaned Data:")
print(df.head())

print("\nSales by City:")
print(city_summary.head())

print("\nSales by Category:")
print(category_summary.head())

print(df.head())
