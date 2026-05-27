## Task 1

import sqlite3


try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")
except sqlite3.Error as e:
    print(f"Error ocurred: {e}")


## Task 2

try:
    with sqlite3.connect("../db/magazines.db") as conn:

        conn.execute("PRAGMA foreign_keys = ON;")
        
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS publishers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT NOT NULL UNIQUE
                    )
                    """)
        
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS magazines (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT NOT NULL UNIQUE,
                        publisher_id INTEGER,
                        FOREIGN KEY(publisher_id) REFERENCES publishers(id)
                    )
                    """)
        
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS subscribers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        publisher_id INTEGER,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL,
                        FOREIGN KEY(publisher_id) REFERENCES publishers(id)
                    )
                    """)
        
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS subscriptions (
                        subscriber_id INTEGER,
                        magazine_id INTEGER,
                        expiration_date TEXT NOT NULL,
                        FOREIGN KEY(subscriber_id) REFERENCES subscribers(id)
                        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
                        UNIQUE (subscriber_id, magazine_id)
                    )
                    """)
        
        print("Tables created successfully.")

except sqlite3.Error as e:
    print(f"Error ocurred: {e}")