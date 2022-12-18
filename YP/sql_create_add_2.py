import sqlite3

con = sqlite3.connect('mov.sqlite')
cur = con.cursor()

# -1 Create table-
cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);
''')

movies = [
    (1, 'Весёлые мелодии', 'Мультсериал', 1930),
    (2, 'Кто подставил кролика Роджера', 'Фильм', 1988),
    (3, 'Безумные Мелодии Луни Тюнз', 'Мультсериал', 1931),
    (4, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969),
    (5, 'Хороший, плохой, злой',	'Фильм',	1967),
    (6, 'Последний киногерой',	'Фильм',	1993),
    (7, 'Она написала убийство',	'Сериал',	1984),
    (8, 'Лас-Вегас',	'Сериал',	2003),
    (9, 'Паркер Льюис не проигрывает',	'Сериал',	1990),
    (10, 'Койот против Acme',	'Фильм', 2023),
]

# -2 Insert data-
cur.executemany('INSERT INTO movies VALUES(?, ?, ?, ?);', movies)

# Send queries, save changes
con.commit()
# Close connect
con.close() 