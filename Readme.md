# Inventory Management System

## Description

This project implements a comprehensive Inventory Management System in Python, utilizing SQLite for data management and Tkinter for creating an intuitive graphical interface. The system allows users to add, view, update, and delete items in their home inventory, as well as search for specific items.

## Features

*   Database:
        SQLite used to create and manage the local database.
        "Inventory" table structure with fields for item name, location, description, brand, purchase date, and purchase value.
        Implementation of CRUD (Create, Read, Update, Delete) operations for inventory items.
        Efficient integration with SQLite using connections and cursors for queries and updates.
        Transaction management to ensure data consistency.

*   Graphical Interface:
        User-friendly and intuitive interface developed with Tkinter.
        Entry fields for adding and editing item data.
        Buttons for performing CRUD operations and searching for items.

*   Available Operations:
        Add Item: Adds a new item to the inventory by filling in all required fields.
        View Items: Lists all items present in the inventory along with their respective information.
        Update Item: Edits the information of a selected item, updating the fields as needed.
        Delete Item: Removes a specific item from the inventory after user confirmation.
        Search Item: Searches for a specific item by ID and returns its details.

## Database Structure

The database has a single table called "Inventory" with the following fields:

        id: (INTEGER, auto-incrementing primary key)
        name: (TEXT, item name)
        location: (TEXT, location of the item in the residence)
        description: (TEXT, detailed description of the item)
        brand: (TEXT, brand of the item)
        date_of_purchase: (TEXT, date of purchase of the item)
        purchase_value: (REAL, purchase value of the item)

## Running the Inventory Management System

* Installation:

        Clone or Download the Project
        Install Required Libraries

* Runing the Program 

        Create the Database:

            python3 db.py

        Run the main program:

            python3 main.py