import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create/connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
);
""")

# Step 3: Insert sample data
sample_data = [
    ('Ring', 10, 199.99),
    ('Necklace', 5, 299.99),
    ('Bracelet', 8, 149.99),
    ('Earrings', 12, 99.99),
    ('Pendant', 7, 129.99)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?);", sample_data)
conn.commit()

# Step 4: Run SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
"""
df = pd.read_sql_query(query, conn)

# Step 5: Print result
print("Sales Summary:")
print(df)

# Step 6: Plot bar chart
plt.figure(figsize=(8, 5))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("sales_chart.png")
plt.show()

# Step 7: Close the connection
conn.close()
