import sqlite3
import json
from datetime import datetime
from models import User

USERS = [
    {
        'id': 1,
        'first_name': 'Rob',
        'last_name': 'Zombie',
        'username': 'Zomboy',
        'password': 'r0b',
        'email': 'robo@mail.com',
        'bio': 'More Human than Human',
        'created_on': datetime.now(),
        'active': 1
    },
    {
        'id': 2,
        'first_name': 'Roman',
        'last_name': 'Reigns',
        'username': 'Champ',
        'password': 'rrc',
        'email': 'roman@mail.com',
        'bio': 'You\'re either with me or against me',
        'created_on': datetime.now(),
        'active': 1
    },
    {
        'id': 3,
        'first_name': 'Josh',
        'last_name': 'Blue',
        'username': 'Twitch',
        'password': 'bl00',
        'email': 'jb@mail.com',
        'bio': 'Olympic Comedian',
        'created_on': datetime.now(),
        'active': 1
    }
]

def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True and the user's id as the token
                     If the user was not found will return valid boolean False
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from Users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)


def create_user(user):
    """Adds a user to the database when they register

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (first_name, last_name, username, email, password, bio, created_on, active) values (?, ?, ?, ?, ?, ?, ?, 1, 1)
        """, (
            user['first_name'],
            user['last_name'],
            user['username'],
            user['email'],
            user['password'],
            user['bio'],
            datetime.now()
        ))

        id = db_cursor.lastrowid
        print(id)
        # Return the dictionary with `id` property added
        return json.dumps({
            'token': id,
            'valid': True
        })

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.first_name,
            a.last_name,
            a.username,
            a.password,
            a.email,
            a.bio,
            a.created_on
        FROM users a
        """)

        # Initialize an empty list to hold all user representations
        users = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an user instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # user class above.
            user = User(row['id'], row['first_name'], row['last_name'],
                            row['username'], row['email'], row['password'],
                            row['bio'], row['created_on'])

            users.append(user.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(users)
