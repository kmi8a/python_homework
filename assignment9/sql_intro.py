import sqlite3

## Task 3 (3.2 - functions)

def populate_publishers(connection, publisher_name):
    cursor = connection.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))
    results = cursor.fetchone()

    if results:
        print(f"Publisher: {publisher_name} already exists.")
        return

    connection.execute("INSERT INTO publishers (name) VALUES (?)", (publisher_name,))
    print(f"Publisher: {publisher_name} succesfully added.")     

def populate_magazines(connection, magazine_name, publisher_name):
    cursor = connection.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))

    results = cursor.fetchone()

    if results:
        print(f"Magazine: {magazine_name} already exists.")
        return
    
    cursor = connection.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))

    row = cursor.fetchone()

    if row:
        publisher_id = row[0]

        connection.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (magazine_name, publisher_id))
        print(f"{magazine_name} succesfully added under publisher: {publisher_name}.")
    else:
        print(f"Publisher {publisher_name} doesn't exists")

def populate_subscribers(connection, subscriber_name, subscriber_address):
    cursor = connection.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))

    results = cursor.fetchone()

    if results:
        print(f"Subscriber: {subscriber_name} information already exists.")
        return

    connection.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (subscriber_name, subscriber_address))
    print(f"Subscriber: {subscriber_name} information succesfully added.")
        

def populate_subscriptions(connection, subscriber_name, magazine_name, expiration_date):
    cursor = connection.execute("SELECT id FROM subscribers WHERE name = ?", (subscriber_name,))

    subscriber_result = cursor.fetchone()

    if not subscriber_result:
        print(f"Subscriber: {subscriber_name} doesn't exists in the database.")
        return
    
    subscriber_id = subscriber_result[0]

    cursor = connection.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))

    magazine_result = cursor.fetchone()

    if not magazine_result:
        print(f"Magazine: {magazine_name} doesn't exists in the database.")
        return

    magazine_id = magazine_result[0]

    try:
        connection.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
        print(f"Subscriber: {subscriber_name} added a {magazine_name} subscription.")
    except sqlite3.IntegrityError:
        print(f"Subscriber: {subscriber_name} already has an existing subscription to {magazine_name}.")


## Task 1

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")

        ## Task 2

        conn.execute("PRAGMA foreign_keys = ON")
        
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
                        name TEXT NOT NULL,
                        address TEXT NOT NULL
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

        ## Task 3 (3.3 - Populate tables)

        populate_publishers(conn, 'Conde Nast')
        populate_publishers(conn, 'Disney')
        populate_publishers(conn, 'Hearst')

        populate_magazines(conn, 'GQ', 'Conde Nast')
        populate_magazines(conn, 'Glamour', 'Conde Nast')
        populate_magazines(conn, 'The New Yorker', 'Conde Nast')

        populate_magazines(conn, 'National Geographic', 'Disney')
        populate_magazines(conn, 'Marvel Comics', 'Disney')
        populate_magazines(conn, 'Vanity Fair', 'Disney')

        populate_magazines(conn, 'Esquire', 'Hearst')
        populate_magazines(conn, "Road & Track", 'Hearst')
        populate_magazines(conn, 'Popular Mechanics', 'Hearst')

        populate_subscribers(conn, 'Camilo', '123 Maple st')
        populate_subscribers(conn, 'Nathalia', '567 Catawba st')
        populate_subscribers(conn, 'Oswaldo', '14 Theresa ln')

        populate_subscriptions(conn, 'Camilo', 'Popular Mechanics', '5/28/2027')
        populate_subscriptions(conn, 'Nathalia', 'Vanity Fair', '9/15/2026')
        populate_subscriptions(conn, 'Oswaldo', 'The New Yorker', '12/31/2027')

        ## Task 4

        cursor = conn.execute("SELECT * FROM subscribers")
        subscribers_result = cursor.fetchall()
        print(subscribers_result)

        cursor = conn.execute("SELECT name FROM magazines ORDER BY name")
        magazines_result = cursor.fetchall()

        print(magazines_result)

        cursor = conn.execute("SELECT magazines.name FROM magazines JOIN publishers ON publishers.id = magazines.publisher_id WHERE publishers.name = 'Disney'")
        magazines_by_publisher = cursor.fetchall()

        print(magazines_by_publisher)


except sqlite3.Error as e:
    print(f"Error ocurred: {e}")




