import sqlite3
import json
from models import Posts, Users

POSTS = [
    {
        "id": 1,
        "category_id": 1,
        "publication_date": "11.04.2022",
        "image_url": "https://images.unsplash.com/photo-1531260796528-ae45a644fb20?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8c2FkJTIwbW9vZHxlbnwwfHwwfHw%3D&w=1000&q=80",
        "content": "I am sad bc this sucks sometimes",
        "approved": 1
    }]

def create_post(post):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (id, category_id, title, publication_date, image_url, content, approved) values (?, ?, ?, ?, ?, ?, 1)
        """, (
            post['category_id'],
            post['title'],
            post['publication_date'],
            post['image_url'],
            post['content'],
            post['approved'],
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })

def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        """)

        # Initialize an empty list to hold all user representations
        post = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:
        posts = Posts(row['id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])

        post.append(posts.__dict__)


    return json.dumps(post)

def get_single_post(id):
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        # Convert rows of data into a Python list
        data = db_cursor.fetchone()

        post = Posts(data['id'], data['category_id'], data['title'], data['publication_date'], data['image_url'], data['content'], data['approved'])


    return json.dumps(post.__dict__)

def create_post(post):
    """docstring"""
    # Get the id value of the last post in the list
    max_id = POSTS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the post dictionary
    post["id"] = new_id

    # Add the post dictionary to the list
    POSTS.append(post)

    # Return the dictionary with `id` property added
    return post

def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))

def update_post(id, new_post):
    """docstring"""
    # Iterate the postS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, post in enumerate(POSTS):
        if post["id"] == id:
            # Found the post. Update the value.
            POSTS[index] = new_post
            break
