import sqlite3
import json
from models import Post

def get_all_posts():
  with sqlite3.connect('./db.sqlite3') as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.content,
        p.approved
    FROM Posts p
    """)
    
    posts = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['content'], row['approved'])
      
      posts.append(post.__dict__)
    
    return json.dumps(posts)

def get_single_post(id):
    with sqlite3.connect('./db.sqlite3') as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      SELECT
          p.id,
          p.user_id,
          p.category_id,
          p.title
      """)

def delete_post(id):
  pass

def update_post(id, new_post):
  pass

def get_posts_by_user(id, user_id):
  pass
