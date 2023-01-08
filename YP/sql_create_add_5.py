import sqlite3

con = sqlite3.connect('mov.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS movies1(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS directors1(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS directors_movies1(    
    director_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    -- Пару полей назначаем композитным первичным ключом
    -- эта пара уникальна в пределах таблицы
    PRIMARY KEY (director_id, movie_id),
    FOREIGN KEY(director_id) REFERENCES directors1(id),
    FOREIGN KEY(movie_id) REFERENCES movies1(id)
);
''')

con.commit()
con.close()