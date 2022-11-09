import sqlite3
import json
from models import Posts, Reactions, PostReaction

def get_reactions_of_post(post_id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            r.id,
            r.reaction_id,
            r.user_id,
            r.post_id,
        FROM PostReactions r
        WHERE r.post_id = ?
         """, ( post_id, ))

        post_reactions = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post_reaction = PostReaction(row['id'], row['reaction_id'], row['user_id'], row['post_id'])

            post_reactions.append(post_reaction.__dict__)

    return json.dumps(post_reactions)

def add_reaction_to_post():
    pass

def update_reaction_to_post():
    pass

def remove_reaction_from_post():
    pass
