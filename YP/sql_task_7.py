import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS ice_cream8(
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);

ALTER TABLE ice_cream8
ADD COLUMN is_published INTEGER;

ALTER TABLE ice_cream8
ADD COLUMN is_on_main INTEGER;
''')

# SQLite 3.26+
# cur.execute('''
# ALTER TABLE ice_cream8
# RENAME COLUMN name TO specification
# ''')

# cur.executescript('''
# DROP TABLE ice_cream8;
# ''')

con.commit()
con.close()