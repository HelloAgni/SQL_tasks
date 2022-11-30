import sqlite3

# Create or connect to db
con = sqlite3.connect('db.sqlite')

# Create Resident base in memory (for Debug, Tests)
# con = sqlite3.connect(':memory:')

# Object cursor
cur = con.cursor()

# --Create table--

# -Version 1-
cur.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday_year INTEGER
);
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);
''')

# -Create table-
# cur.execute("CREATE TABLE IF NOT EXISTS zero(id PRIMARY KEY, text TEXT)")
# -Delete table-
# cur.execute("DROP TABLE zero")

# -Version 2-
# -Create table with cur.executescript-
# cur.executescript('''
# CREATE TABLE IF NOT EXISTS directors(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     bithday_year INTEGER
# );

# CREATE TABLE IF NOT EXISTS movies(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     type TEXT,
#     release_year INTEGER
# );
# ''')


# --Add data in table--
# -Add data Version 1-
# cur.execute('''
# INSERT INTO movies(id, name, type, release_year)
# VALUES (1, 'Весёлые мелодии', 'Мультсериал', 1930);
# ''')

# -Add data Version 2-
# cur.execute(
#     'INSERT INTO movies VALUES(?, ?, ?, ?);',
#     (1, 'Весёлые мелодии', 'Мультсериал', 1930)
# )

# -Add data Version 3 many-
directors = [
    (1, 'Текс Эйвери', 1908),
    (2, 'Роберт Земекис', 1952),
    (3, 'Джерри Чиникей', 1912),
]
movies = [
    (1, 'Весёлые мелодии', 'Мультсериал', 1930),
    (2, 'Кто подставил кролика Роджера', 'Фильм', 1988),
    (3, 'Безумные Мелодии Луни Тюнз', 'Мультсериал', 1931),
    (4, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969),
]

cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?, ?);', movies)

# Send queries, save changes
con.commit()
# Close connect
con.close() 