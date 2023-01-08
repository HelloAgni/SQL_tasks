import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Inspect SQL version
cur.execute('''
SELECT sqlite_version();
''')
print([x for x in cur])

# Inspect SQLite_db and get all tables names
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables_name = [x[0] for x in cur]
print(tables_name)  # -> ['directors', 'movies']

# Inspect Postgres_db and get all tables names
"""
SELECT * FROM information_schema.tables WHERE table_schema = 'public';
"""

# Inspect SQLite_db table and get all types of rows
# SELECT * FROM sqlite_master
cur.execute('''
SELECT sql
FROM sqlite_master
WHERE name='ice_cream';
''')
info = [x[0] for x in cur]
print(info[0])  # -> name TEXT, category TEXT

# Inspect Postgres_db table and get name and all types of rows
"""
SELECT column_name,
       data_type
FROM
    information_schema.columns
WHERE
    table_schema = 'public' AND 
    table_name = '<YOUR_TABLE>';
"""

# Get SQLite_db all rows name from table number 1
cur.execute(f"SELECT * FROM '{tables_name[0]}'")
rows_name = [x[0] for x in cur.description]
print(rows_name)  # ['id', 'name', 'birthday_year']
con.close() 