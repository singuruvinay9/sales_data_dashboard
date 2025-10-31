import pandas as pd

# Load the CSV
df = pd.read_csv(r"C:\Users\Vinay\Downloads\archive (1)\superstore.csv", encoding='latin1')


# Show top 5 rows
print(df.head())

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Add Month & Year for time-based trends
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

# Add Profit Margin
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# Remove null or invalid values if any
df.dropna(inplace=True)

# Save clean data
df.to_csv("clean_sales_data.csv", index=False)
print("✅ Cleaned file saved as clean_sales_data.csv")
