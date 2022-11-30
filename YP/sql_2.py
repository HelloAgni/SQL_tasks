import sqlite3

con = sqlite3.connect('db2.sqlite')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS ice_cream(
    name TEXT,
    description TEXT,
    category TEXT
)
''')

# Send queries, save changes
con.commit()
# Close connect
con.close() 