import sqlite3
import json
from datetime import datetime
from models import Subscriptions

def get_all_subscriptions():
    """this is a docstring"""
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            s.id,
            s.author_id,
            s.follower_id,
            s.created_on
        FROM Subscriptions s
        """)

        # Initialize an empty list to hold all user representations
        subscriptions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:
        subscription_list = Subscriptions(row['id'], row['author_id'], row['follower_id'], row['created_on'])

        subscriptions.append(subscription_list.__dict__)

    return json.dumps(subscriptions)


def create_subscription(subscription):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (author_id, follower_id, created_on) values (?, ?, 1)
        """, (
            subscription['author_id'],
            subscription['follower_id'],
            datetime.now()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })
