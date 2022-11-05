import sqlite3
import json
from models import Categories

def get_all_categories():
    """this is a docstring"""
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)

        # Initialize an empty list to hold all user representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:
        category_list = Categories(row['id'], row['label'])

        categories.append(category_list.__dict__)

    return json.dumps(categories)

def get_single_categories(id):
    """docstring"""
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        WHERE c.id = ?
        """, ( id, ))

        # Convert rows of data into a Python list
        data = db_cursor.fetchone()

        categories = Categories(data['id'], data['label'])


    return json.dumps(categories.__dict__)


def delete_categories(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
        """, (id, ))
