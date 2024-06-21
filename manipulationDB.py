import sqlite3 as lite


# create connection
connection = lite.connect("inventory/database.db")

""" CRUD (create, read, update, delete) """

# insert data
def insert_form(insert_data):
    """ Insert new data in the Inventory table """
    with connection:
        cursor = connection.cursor()
        query = "INSERT INTO Inventory (name, location, description, brand, date_of_purchase, purchase_value) VALUES (?,?,?,?,?,?)"
        cursor.execute(query, insert_data)

# view datas
def view_inventory():
    """ Returns a list containing all items in the Inventory table """
    inventory = []
    with connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Inventory"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            inventory.append(row)
    return inventory

# Update datas
def update_form(update_data):
    """ Updates the data of an item in the Inventory table """
    with connection:
        cursor = connection.cursor()
        query = "UPDATE Inventory SET name=?, location=?, description=?, brand=?, date_of_purchase=?, purchase_value=? WHERE id=?"
        cursor.execute(query, update_data)

# Delete data
def delete_form(delete_data):
    """ Deletes an item from the Inventory table """
    with connection:
        cursor = connection.cursor()
        query = "DELETE FROM Inventory WHERE id=?"
        cursor.execute(query, delete_data)


# View data
def view_item(id):
    """ Returns a specific item from the Inventory table based on the ID  """
    with connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Inventory WHERE id=?"
        cursor.execute(query, id)
        return cursor.fetchone()