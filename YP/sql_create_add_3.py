import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS categories4(
id INTEGER PRIMARY KEY,
slug TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ice_cream4(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
description TEXT,
price REAL NOT NULL,
category_id INTEGER NOT NULL,
FOREIGN KEY(category_id) REFERENCES categories4(id)
);
''')

ice = [
    (1, 'Пивное мороженое', 'Со вкусом светлого нефильтрованного лагера.', 500.0, 1),
    (2, 'Мороженое с кузнечиками', 'В колумбийском стиле: с добавлением карамелизованных кузнечиков.', 688.0, 1),
    (3, 'Мороженое со вкусом сыра чеддер', 'Вкус настоящего сыра в вафельном стаканчике.', 500.0, 1),
    (4, 'Пломбир 1937', 'Пломбир по рецепту 1937 года Московского хладокомбината.', 78.0, 2),
    (5, 'Томатное мороженое', 'В СССР делали и томатное мороженое тоже. Вкус специфический.', 0.1, 2)
]

c = [
    (1, 'exotic'),
    (2, 'normal')
]

cur.executemany('INSERT INTO ice_cream4 VALUES(?, ?, ?, ?, ?);', ice)
cur.executemany('INSERT INTO categories4 VALUES(?, ?);', c)

con.commit()
con.close()