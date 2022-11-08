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
        ORDER BY s.created_on DESC
        """)
        # Initialize an empty list to hold all user representations
        subscriptions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:
        subscription_list = Subscriptions(row['id'], row['author_id'], row['follower_id'], row['created_on'])

        # user = Users(row['id'], row['first_name'], row['last_name'], row['email'], row['bio'], row['profile_image_url'], row['created_on'], row['active'], row['password'])
        # # Add the dictionary representation of the users to the posts
        # subscription_list.user = user.__dict__

        subscriptions.append(subscription_list.__dict__)

    return json.dumps(subscriptions)

def get_single_subscription(id):
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
        WHERE s.id = ?
        """, ( id, ))

        # Convert rows of data into a Python list
        data = db_cursor.fetchone()
        subscription_list = Subscriptions(data['id'], data['author_id'], data['follower_id'], data['created_on'])

    return json.dumps(subscription_list.__dict__)

def create_subscription(new_subscription):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions (author_id, follower_id, created_on) values (?, ?, ?)
        """, (
            new_subscription['author_id'],
            new_subscription['follower_id'],
            datetime.now()
        ))

        id = db_cursor.lastrowid
        new_subscription['id'] = id
    return json.dumps(new_subscription)

def delete_subscription(id):
    """docstring
        """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM subscriptions
        WHERE id = ?
        """, (id, ))

def update_subscription(id, new_subscription):
    """docstring"""
    # Iterate the subscriptions list, but use enumerate() so that
    # you can access the index value of each item.
    pass

def get_subscription_by_user(subscription_id):
    pass
