import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Inspect db and get all tables names
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables_name = [x[0] for x in cur]
print(tables_name)  # -> ['directors', 'movies']

# Get all rows name from table number 1
cur.execute(f"SELECT * FROM '{tables_name[0]}'")
rows_name = [x[0] for x in cur.description]
print(rows_name)  # ['id', 'name', 'birthday_year']
con.close() 