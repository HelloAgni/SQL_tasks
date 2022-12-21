import sqlite3

con = sqlite3.connect('db2.sqlite')
cur = con.cursor()

cur.execute("""
SELECT movies.name,
       slogans.name
FROM movies, 
     slogans
WHERE movies.slogan_id = slogans.id; 
""")
for items in cur:
    print(items)

# INNER JOIN
cur.execute('''
SELECT *
FROM movies
JOIN slogans ON movies.slogan_id = slogans.id; 
''')
for items in cur:
    print(items)

# INNER JOIN
cur.execute('''
SELECT movies.name,
       slogans.name,
       types.name
FROM movies
JOIN slogans ON movies.slogan_id = slogans.id
JOIN types ON movies.type_id = types.id;
''')
for items in cur:
    print(items)

# LEFT JOIN
cur.execute('''
SELECT movies.name,
       slogans.name
FROM movies
LEFT JOIN slogans ON movies.slogan_id = slogans.id; 
''')
for items in cur:
    print(items)

# RIGHT JOIN - SQLite doesn't support RIGHT and FULL OUTER JOINs
# cur.execute('''
# SELECT movies.name,
#        types.name
# FROM movies
# RIGHT JOIN types ON movies.type_id = types.id; 
# ''')
# for items in cur:
#     print(items)

# Change for SQLite - instead RIGHT JOIN >
cur.execute('''
SELECT movies.name,
       types.name
FROM types
LEFT JOIN movies ON movies.type_id = types.id; 
''')
for items in cur:
    print(items)

# FULL JOIN
# cur.execute('''
# SELECT movies.name,
#        slogans.name
# FROM movies
# FULL JOIN slogans ON movies.slogan_id = slogans.id; 
# ''')
# for items in cur:
#     print(items)

# FULL JOIN - SQL doesn't support RIGHT and FULL OUTER JOINs
# Change for SQLite - instead FULL JOIN
cur.execute('''
SELECT movies.name,
       slogans.name
FROM movies
LEFT JOIN slogans ON movies.slogan_id = slogans.id
UNION
SELECT movies.name,
       slogans.name
FROM slogans
LEFT JOIN movies ON movies.slogan_id = slogans.id; 
''')
for items in cur:
    print(items)

# CROSS JOIN
cur.execute('''
SELECT movies.name,
       slogans.name
FROM movies
CROSS JOIN slogans; 
''')
for items in cur:
    print(items)

con.commit()
con.close()