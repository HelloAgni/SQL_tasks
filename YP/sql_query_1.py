import sqlite3

con = sqlite3.connect('mov.sqlite')
cur = con.cursor()

# WHERE
items_1 = cur.execute('''
SELECT name,
       release_year
FROM movies
WHERE release_year > 1980; 
''')
print('WHERE')
print(*[x for x in items_1], sep='\n')

# ORBER BY (ASC, DESC)
items_2 = cur.execute('''
SELECT name,
       release_year
FROM movies
WHERE release_year > 1980
ORDER BY release_year DESC;
''')
print('ORBER BY')
print(*[x for x in items_1], sep='\n')

# ORBER BY 2 rows
items_3 = cur.execute('''
SELECT type,
       name
FROM movies
WHERE release_year > 1980
ORDER BY type DESC, name;
''')
print('ORBER BY 2 rows')
print(*[x for x in items_3], sep='\n')

# LIMIT
items_4 = cur.execute('''
SELECT name,
       type
FROM movies
ORDER BY name
LIMIT 2;
''')
print('LIMIT')
print(*[x for x in items_4], sep='\n')

# LIMIT <records> OFFSET <shift selection>
items_5 = cur.execute('''
SELECT name,
       type
FROM movies
ORDER BY name
LIMIT 2 OFFSET 2;
''')
print('LIMIT and OFFSET')
print(*[x for x in items_5], sep='\n')

# COUNT
items_6 = cur.execute('''
SELECT COUNT(id)
FROM movies;
''')
print('COUNT')
print(*[x for x in items_6], sep='\n')

# MIN, MAX
items_7 = cur.execute('''
SELECT MIN(release_year), MAX(release_year)
FROM movies;
''')
print('MIN and MAX')
print(*[x for x in items_7], sep='\n')

# AVG, SUM
items_8 = cur.execute('''
SELECT AVG(release_year), SUM(release_year)
FROM movies
WHERE id > 3;
''')
print('AVG and SUM')
print(*[x for x in items_8], sep='\n')

# Send queries, save changes
con.commit()
# Close connect
con.close() 