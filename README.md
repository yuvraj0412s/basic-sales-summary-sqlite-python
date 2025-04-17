# 📊 Basic Sales Summary using SQLite and Python

This project demonstrates how to create and analyze a simple sales database using SQLite, SQL queries, and Python. The goal is to calculate total quantity sold and revenue per product and visualize the results with a bar chart.

---

## 🎯 Objective

- Create a small sales database using SQLite
- Perform simple SQL aggregations using Python
- Display the results using Pandas and Matplotlib

---

## 🧰 Tools Used

- Python (Jupyter Notebook / .py script)
- SQLite (built-in with Python)
- pandas
- matplotlib

---

## 🛠️ Steps Performed

1. **Created a SQLite database** with a `sales` table.
2. **Inserted sample product data** including quantity and price.
3. **Executed SQL queries** to compute:
   - Total quantity sold per product
   - Total revenue per product (quantity × price)
4. **Loaded the results into Pandas** for analysis.
5. **Displayed results** using `print()` and a `matplotlib` bar chart.
6. **Saved chart** as a PNG image.

---

## 📝 Sample SQL Query Used

```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
