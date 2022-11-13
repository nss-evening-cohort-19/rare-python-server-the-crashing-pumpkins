import sqlite3
import json

from models import Tags

def get_all_tags():
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        """)

        # Initialize an empty list to hold all user representations
        tag = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:
        tags = Tags(row['id'], row['label'])

        tag.append(tags.__dict__)


    return json.dumps(tag)

def get_single_tag(id):
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        WHERE t.id = ?
        """, ( id, ))

        # Convert rows of data into a Python list
        data = db_cursor.fetchone()

        tag = Tags(data['id'], data['label'])


    return json.dumps(tag.__dict__)

def create_tag(new_tag):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? )
                    """, (
                    new_tag['label'],

        ))

        id = db_cursor.lastrowid
        new_tag['id'] = id
    return json.dumps(new_tag)

def delete_tag(id):
    """String of the Doc"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Tags
        WHERE id = ?
        """, ( id, ))

def update_tag(id, fresh_tag):
    """Dr.String"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Tags
            SET
            label = ?
        WHERE id = ?
        """, (
            fresh_tag['label'],
            id,
        ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
