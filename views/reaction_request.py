import sqlite3
import json
from models import Reactions, PostReaction

def get_reactions_of_post(post_id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            pr.id as pr_id,
            pr.reaction_id,
            pr.user_id,
            pr.post_id,
            r.id,
            r.label,
            r.image_url
        FROM PostReactions pr
        LEFT JOIN Reactions r
            ON pr.reaction_id = r.id
        WHERE pr.post_id = ?
         """, ( post_id, ))

        post_reactions = []

        dataset = db_cursor.fetchall()
        for row in dataset:
            post_reaction = Reactions(row['id'], row['label'], row['image_url'])

            post_reaction.user_id = row['user_id']

            post_reactions.append(post_reaction.__dict__)

    return json.dumps(post_reactions)

def create_reaction(new_reaction):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Reactions(label, image_url)
        VALUES (?, ?)
        """, (
            new_reaction['label'],
            new_reaction['image_url']
        ))
        
        id = db_cursor.lastrowid
        new_reaction['id'] = id
        
    return json.dumps(new_reaction)

def create_post_reaction(new_preaction):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostReactions (user_id, reaction_id, post_id)
        VALUES (?, ?, ?)
        """, (
            new_preaction['user_id'],
            new_preaction['reaction_id'],
            new_preaction['post_id']
        ))

        id = db_cursor.lastrowid
        new_preaction['id'] = id

    return json.dumps(new_preaction)
