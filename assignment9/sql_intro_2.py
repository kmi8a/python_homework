## Task 5

import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = "SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price FROM products p JOIN line_items li ON li.product_id = p.product_id;"
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())

df['total'] = df['quantity'] * df['price']
print(df.head())

df = df.groupby('product_id').agg({'line_item_id':'count', 'total':'sum', 'product_name': 'first'})
print(df.head())

df = df.sort_values(by='product_name')
print(df.head())

df.to_csv('order_summary.csv', index=False)