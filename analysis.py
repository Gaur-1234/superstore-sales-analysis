import sys
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries loaded successfully")

df = pd.read_csv("superstore.csv")
# Rename column to something readable
df = df.rename(columns={"记录数": "Record_Count"})

# Convert to datetime
df["Order.Date"] = pd.to_datetime(df["Order.Date"])
df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

df["Month"] = df["Order.Date"].dt.month

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("sales_by_category.png") 

plt.show()

# Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar", color="orange")

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.savefig("Profit_by_region.png") 

plt.show()

# Top 10 Products by Sales
top_products = df.groupby("Product.Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("Product_by_Sales.png") 

plt.show()

# Sales by Year
year_sales = df.groupby("Year")["Sales"].sum()

plt.figure(figsize=(8,5))
year_sales.plot(marker="o")

plt.title("Sales Trend by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.savefig("sales_by_year.png") 

plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Discount", y="Profit", data=df)

plt.title("Profit vs Discount")
plt.savefig("Profit_vs_Discount.png") 
plt.show()

pivot = df.pivot_table(values="Sales", index="Region", columns="Category", aggfunc="sum")

plt.figure(figsize=(8,5))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm")

plt.title("Sales Heatmap by Region and Category")
plt.savefig("Heatmap_by_region.png") 
plt.show()
