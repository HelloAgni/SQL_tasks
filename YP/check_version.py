import sqlite3

con = sqlite3.connect('new.sqlite')
cur = con.cursor()

# Inspect SQL version
cur.execute('''
SELECT sqlite_version();
''')
print([x for x in cur])