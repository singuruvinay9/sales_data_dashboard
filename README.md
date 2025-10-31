# 📊 Sales Data Dashboard

## 🧠 Project Overview
This project demonstrates how to **analyze and visualize sales data** using **Python** and **Power BI** to help decision-makers understand business performance through KPIs, trends, and region-wise breakdowns.

## 🎯 Objective
To visualize sales data in a way that highlights:
- Total Sales, Profit, and Quantity
- Performance trends over time
- Regional and category-based comparisons

## 🧰 Tools & Technologies Used
| Tool | Purpose |
|------|----------|
| 🐍 **Python (Pandas)** | Data cleaning and transformation |
| 📈 **Power BI** | Dashboard creation and visualization |
| 📊 **Excel / CSV** | Raw data source |
| 💻 **GitHub** | Project hosting and version control |

## 🗂️ Dataset Information
**Dataset:** `Sample - Superstore.csv`  
**Source:** Kaggle  
**Columns Include:**
- Order ID, Product Name, Category, Sub-Category  
- Sales, Profit, Quantity, Discount  
- Order Date, Ship Mode, Region, Customer Segment  

## ⚙️ Project Workflow

### 1️⃣ Data Cleaning (Python)
**File:** `clean_data.py`

**Key Steps:**
```python
import pandas as pd

# Load data
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Clean data
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Save clean file
df.to_csv("clean_sales_data.csv", index=False)
```

**Output File:** `clean_sales_data.csv` ✅

### 2️⃣ Data Visualization (Power BI)

**Steps in Power BI:**
1. Imported `clean_sales_data.csv`
2. Created KPI cards for:
   - 💰 Total Sales  
   - 📈 Total Profit  
   - 📦 Total Quantity  
3. Built charts:
   - 📊 Bar Chart → *Sales by Category*
   - 🥧 Pie Chart → *Profit by Region*
   - 📈 Line Chart → *Sales Trend Over Time*
4. Designed an interactive dashboard layout
5. Applied filters and labels for clarity

**Report File:** `Sales_Dashboard.pbix`

## 📊 Dashboard Highlights

| Visual | Description |
|--------|--------------|
| 💰 **KPI Cards** | Show overall Sales, Profit, and Quantity |
| 📊 **Bar Chart** | Category-wise Sales comparison |
| 🥧 **Pie Chart** | Profit distribution across Regions |
| 📈 **Line Chart** | Sales trend over months/years |

## 📈 Key Insights
- **Technology** category generated the highest sales.  
- **West** region contributed the most profit.  
- Sales show an upward trend during **year-end months**.  
- Discounts have a noticeable effect on overall profitability.

## 🧾 Project Structure
```
Sales_Data_Dashboard_Project/
│
├── data/
│   ├── Sample - Superstore.csv
│   ├── clean_sales_data.csv
│
├── code/
│   ├── clean_data.py
│
├── report/
│   ├── Sales_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard_view.png
│   ├── visuals_overview.png
│
└── README.md
```

## 🎥 Demo
*(Add your short video or screenshot links here)*  
Example: [Demo Video Link](https://your-demo-link.com)

## 🔗 GitHub Repository
👉 [View Complete Project on GitHub](https://github.com/YOUR_USERNAME/Sales-Data-Dashboard)

## 👨‍💻 Author
**Vinay Singuru**  
📍 Data Science Enthusiast | Power BI & Python Learner  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/singuru-vinay-57050125b)

## 🏁 Conclusion
This project helped demonstrate how to turn raw sales data into **actionable business insights** using **Python for data preparation** and **Power BI for interactive visualization**.  
It reflects a real-world application of data analytics and storytelling through dashboards.

⭐ *If you like this project, give it a star on GitHub!* ⭐
