import numpy as np
import pandas as pd

# Step 1: Create Sample Dataset
data = {
    "Order_ID": np.arange(1, 11),
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop"],
    "Price": [50000, 20000, 15000, 52000, 21000, 14000, 51000, 22000, 13000, 53000],
    "Quantity": [1, 2, 1, 1, 3, 2, 1, 2, 1, 1],
    "Date": pd.date_range(start="2025-01-01", periods=10)
}

df = pd.DataFrame(data)

# Step 2: Data Cleaning
df["Revenue"] = df["Price"] * df["Quantity"]

# Step 3: Basic Analysis
total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Step 4: Group By Product
product_sales = df.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:\n", product_sales)

# Step 5: Monthly Analysis
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Revenue"].sum()
print("\nMonthly Sales:\n", monthly_sales)

# Step 6: Best Selling Product
best_product = product_sales.idxmax()
print("\nBest Selling Product:", best_product)
