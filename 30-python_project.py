import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Fix for plotting (IMPORTANT)
# -------------------------------
import matplotlib
matplotlib.use('Agg')   # Prevents GUI blocking

# -------------------------------
# Load dataset
# -------------------------------
file_path = r"C:\Users\chand\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv"

try:
    df = pd.read_csv(file_path, encoding='latin1')
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print("❌ Error loading file:", e)
    exit()

# -------------------------------
# Basic Info
# -------------------------------
print("\n🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Shape of Data:")
print(df.shape)

print("\n🔹 Columns:")
print(df.columns)

print("\n🔹 Data Types:")
df.info()

print("\n🔹 Statistical Summary:")
print(df.describe())

# -------------------------------
# Missing Values
# -------------------------------
print("\n🔹 Missing Values:")
print(df.isnull().sum())

df.fillna(0, inplace=True)

# -------------------------------
# Remove Duplicates
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# Visualization (Saved as Images)
# -------------------------------

# Histogram
df.hist(figsize=(10, 8))
plt.suptitle("Histogram of Features")
plt.savefig("histogram.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

# Count Plot
if 'Gender' in df.columns:
    plt.figure()
    sns.countplot(x='Gender', data=df)
    plt.title("Gender Count")
    plt.savefig("gender_count.png")
    plt.close()

# -------------------------------
# Save Cleaned Data
# -------------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ EDA Completed Successfully!")
print("📁 Plots saved as PNG files in your project folder.")
