import sqlite3

conn = sqlite3.connect('orders.db')

cur = conn.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  message_chat_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  value TEXT
);
"""
cur.execute(create_users_table)

conn.commit()

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(*all_results, sep = '\n')