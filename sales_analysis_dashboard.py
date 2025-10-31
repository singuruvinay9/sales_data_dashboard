# 📊 Superstore Sales Analysis Dashboard (Python + Power BI Ready)
# Author: Vinay Singuru

# ✅ Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Step 2: Load Data
df = pd.read_csv("clean_sales_data.csv")
print("✅ Data Loaded Successfully!\n")
print(df.head())

# ✅ Step 3: Basic Info
print("\n📌 Dataset Info:")
print(df.info())
print("\n📊 Summary Statistics:")
print(df.describe())

# ✅ Step 4: Check Missing Values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# ✅ Step 5: Basic Insights
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()
print("\n💰 Total Sales: ", total_sales)
print("📈 Total Profit: ", total_profit)
print("📦 Total Quantity Sold: ", total_quantity)

# ✅ Step 6: Category-wise & Region-wise Performance
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

print("\n🏷️ Sales by Category:\n", category_sales)
print("\n🌍 Profit by Region:\n", region_profit)
print("\n👥 Sales by Customer Segment:\n", segment_sales)

# ✅ Step 7: Visualizations
plt.style.use('seaborn-v0_8-whitegrid')

# --- 1️⃣ Sales by Category ---
plt.figure(figsize=(6,4))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="coolwarm")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# --- 2️⃣ Profit by Region ---
plt.figure(figsize=(6,4))
sns.barplot(x=region_profit.index, y=region_profit.values, palette="crest")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()

# --- 3️⃣ Sales by Segment ---
plt.figure(figsize=(6,4))
sns.barplot(x=segment_sales.index, y=segment_sales.values, palette="viridis")
plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_segment.png")
plt.show()

# --- 4️⃣ Sales Over Time ---
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_trend = df.groupby('Order Date')['Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(x='Order Date', y='Sales', data=sales_trend, color='blue')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()

# --- 5️⃣ Discount vs Profit ---
plt.figure(figsize=(6,4))
sns.scatterplot(x='Discount', y='Profit', data=df, color='red', alpha=0.6)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("discount_vs_profit.png")
plt.show()

# --- 6️⃣ Correlation Heatmap ---
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

print("\n✅ EDA and Visualizations Completed Successfully!")
print("📁 All charts saved as PNG files in your project directory.")
