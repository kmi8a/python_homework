import sqlite3
import os

## Task 1: Complex JOINs with Aggregation

DB_PATH = "../db/lesson.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

try:

    query = """
    SELECT orders.order_id, ROUND(SUM(products.price * line_items.quantity), 2) as total_price
    FROM orders
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
    LIMIT 5
    ;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for order in results:
        print(f"Order ID:{order[0]}, TOTAL PRICE: ${order[1]:.2f}")

except Exception as e:
    print("Error:", e)


# Task 2: Understanding Subqueries

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
            print(f"Customer: {order[0]}, TOTAL PRICE: $0")
        else:
            print(f"Customer: {order[0]}, TOTAL PRICE: ${order[1]:.2f}")

except Exception as e:
    print("Error:", e)


# Task 3:An Insert Transaction Based on Data

customer_id = None
products_ids = []
employee_id = None
current_order_id = None


try:
    customer_query = "SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';"
    cursor.execute(customer_query)
    customer_id = cursor.fetchone()[0]

    products_query = "SELECT product_id FROM products ORDER BY price ASC LIMIT 5;"
    cursor.execute(products_query)
    products_ids = [result[0] for result in cursor.fetchall()]

    employee_query = "SELECT * FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';"
    cursor.execute(employee_query)
    employee_id = cursor.fetchone()[0]

    date = '2026-06-08'

    print(f'Customer ID: {customer_id}')
    print(f"Product ID's: {products_ids}")
    print(f'Employee ID: {employee_id}')

    cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, ?) RETURNING order_id;", (customer_id, employee_id, date))

    current_order_id = cursor.fetchone()[0]

    for product in products_ids:
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);", (current_order_id, product, 5))

    conn.commit()

    order_query = """
        SELECT line_items.line_item_id, line_items.quantity, products.product_name 
        FROM line_items
        JOIN products ON products.product_id = line_items.product_id
        WHERE line_items.order_id = ?;
        """
    cursor.execute(order_query, (current_order_id,))
    order = cursor.fetchall()
    
    print(f'Order ID: {current_order_id}')
    for item in order:
        print(f"""  Item ID:      {item[0]}
  Quantity:     {item[1]}
  Product Name: {item[2]}\n""")
        

except Exception as e:
    print("Error:", e)
    conn.rollback()

# Task 4: Aggregation with HAVING

try:
    order_qty_query = """
        SELECT employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_qty 
        FROM employees 
        JOIN orders ON employees.employee_id = orders.employee_id 
        GROUP BY employees.employee_id 
        HAVING COUNT(orders.order_id) > 5 
        ORDER BY order_qty DESC;
        """
    cursor.execute(order_qty_query)
    order_qty = cursor.fetchall()

    for employee in order_qty:
        print(f"{employee[0]} {employee[1]}, {employee[2]} orders processed")

except Exception as e:
    print("Error:", e)

finally:
    conn.close()