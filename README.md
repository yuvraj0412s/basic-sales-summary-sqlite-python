# 📊 Basic Sales Summary Using SQLite and Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite&logoColor=orange)](https://www.sqlite.org/index.html)
[![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-brightgreen?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-data%20visualization-orange?logo=matplotlib&logoColor=white)](https://matplotlib.org/)

---

## 🚀 Project Overview

This project demonstrates how to use **SQLite** within **Python** to create a small sales database, perform SQL queries to summarize sales data by product, and visualize the results using a bar chart with **Matplotlib**.

By completing this, you gain hands-on experience in:

- Writing basic SQL queries inside Python  
- Importing SQL data into Pandas DataFrames  
- Performing data aggregation and summary  
- Creating simple, clear visualizations for sales insights  

---

## 🧠 SQL Query Used

```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
```

---
## 💡 Features

- Create and connect to a SQLite database  
- Build a sales table and insert sample data programmatically  
- Use SQL to calculate total quantity sold and total revenue per product  
- Display summarized data via console print  
- Generate a clean bar chart of revenue by product  

---

## 🛠️ Tools & Technologies Used

| Tool/Library | Description                             |
|--------------|-------------------------------------|
| Python       | Programming language used              |
| sqlite3      | Built-in SQLite database support      |
| pandas       | Data analysis and SQL query handling  |
| matplotlib   | Data visualization and plotting       |

---

## 📋 How to Run

1. Clone this repository:

```bash
git clone https://github.com/yourusername/sales-summary-sqlite-python.git
cd sales-summary-sqlite-python
python -m venv env
source env/bin/activate      # macOS/Linux
.\env\Scripts\activate       # Windows
pip install pandas matplotlib
python sales_summary.py
