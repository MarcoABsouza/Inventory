import sqlite3 as lite

# create connection
connection = lite.connect("inventory/database.db")

# create table
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE if not exists Inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, location TEXT, description TEXT, brand TEXT, date_of_purchase DATE, purchase_value DECIMAL)")