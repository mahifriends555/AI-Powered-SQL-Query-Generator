
import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

# Customers
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

# Orders
cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

# Products
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
)
""")

# Order Items
cursor.execute("""
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

# Insert Data
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", [
    (1, "Alice", "Delhi"),
    (2, "Bob", "Mumbai"),
    (3, "Charlie", "Delhi")
])

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", [
    (1, 1, 300, "2024-01-01"),
    (2, 2, 500, "2024-01-02"),
    (3, 1, 200, "2024-01-03")
])

cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", [
    (1, "Laptop", 1000),
    (2, "Phone", 500)
])

cursor.executemany("INSERT INTO order_items VALUES (?, ?, ?, ?)", [
    (1, 1, 1, 1),
    (2, 2, 2, 2),
    (3, 3, 2, 1)
])

conn.commit()
conn.close()

print("Realistic database created!")