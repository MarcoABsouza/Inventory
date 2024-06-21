import sqlite3 as lite

# create connection
connection = lite.connect("inventory/database.db")

# create table
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE if not exists Inventory(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, location TEXT NOT NULL, description TEXT NOT NULL, brand TEXT NOT NULL, date_of_purchase DATE NOT NULL, purchase_value DECIMAL NOT NULL)")