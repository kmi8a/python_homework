import sqlite3
import os

## Task 1: Complex JOINs with Aggregation

DB_PATH = "../db/lesson.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# try:

#     query = """
#     SELECT orders.order_id, ROUND(SUM(products.price * line_items.quantity), 2) as total_price
#     FROM orders
#     JOIN line_items ON orders.order_id = line_items.order_id
#     JOIN products ON line_items.product_id = products.product_id
#     GROUP BY orders.order_id
#     LIMIT 5
#     ;
#     """
#     cursor.execute(query)
#     results = cursor.fetchall()

#     for order in results:
#         print(f"Order ID:{order[0]}, TOTAL PRICE: ${order[1]:.2f}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     conn.close()

## Task 2: Understanding Subqueries

try:

    query = """
    SELECT customers.customer_name, AVG(total_price)
    FROM customers
    LEFT JOIN (
        SELECT orders.customer_id AS customer_id_b, ROUND(SUM(products.price * line_items.quantity), 2) AS total_price
        FROM orders
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
    ) AS subquery
    ON customers.customer_id = subquery.customer_id_b
    GROUP BY customers.customer_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for order in results:
        if order[1] ==  None:
            print(f"Customer:{order[0]}, TOTAL PRICE: $0")
        else:
            print(f"Customer:{order[0]}, TOTAL PRICE: ${order[1]:.2f}")

except Exception as e:
    print("Error:", e)

finally:
    conn.close()