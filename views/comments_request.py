import sqlite3
import json
from models import Comments

def get_all_comments():
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
            c.author_id,
            c.post_id,
            c.content
        FROM Comments c
        """)
        # Initialize an empty list to hold all user representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:
        comment_list = Comments(row['id'], row['author_id'], row['post_id'], row['content'])

        comments.append(comment_list.__dict__)

    return json.dumps(comments)

def get_single_comment(id):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content
        FROM Comments c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        comment_list = Comments(data['id'], data['author_id'], data['post_id'], data['content'])

    return json.dumps(comment_list.__dict__)

def create_comment(new_comment):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments (author_id, post_id, content) values (?, ?, ?)
        """, (
            new_comment['author_id'],
            new_comment['post_id'],
            new_comment['content'],
        ))

        id = db_cursor.lastrowid
        new_comment['id'] = id
    return json.dumps(new_comment)

def delete_comment(id):
    """docstring
        """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

def update_comment(id, new_comment):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Comments
            SET
            author_id = ?,
            post_id = ?,
            content = ?
        WHERE id = ?
        """, (
            new_comment['author_id'],
            new_comment['post_id'],
            new_comment['content'],
            id,
      ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
