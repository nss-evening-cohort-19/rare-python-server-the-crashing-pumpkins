import sqlite3
import json
from models import Reactions, Posts, Users

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

def add_reaction_to_post():
    pass

def update_reaction_to_post():
    pass

def remove_reaction_from_post():
    pass
