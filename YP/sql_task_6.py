import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# For SQLite_db and Postgres_db
"""
CREATE TABLE categories6(
    id INTEGER PRIMARY KEY,
    slug TEXT NOT NULL
);
CREATE TABLE wrappers6(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE ice_cream6(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    wrapper_id INTEGER UNIQUE,
    FOREIGN KEY(category_id) REFERENCES categories6(id),
    FOREIGN KEY(wrapper_id) REFERENCES wrappers6(id)
);

INSERT INTO categories6
VALUES
    (1, 'exotic'),
    (2, 'normal');

INSERT INTO wrappers6
VALUES
    (1, 'Бумажная с черепами'),
    (2, 'Экзотические птицы с яркими перьями'),
    (3, 'Простая упаковка-салфетка с изображением Анфисы и праздничными поздравлениями'),
    (4, 'Упаковка-оригами, незаменима для детских праздников');

INSERT INTO ice_cream6
VALUES
    (1, 'Пивное мороженое', 'Со вкусом светлого нефильтрованного лагера.', 500.0, 1, Null),
    (2, 'Мороженое с кузнечиками', 'В колумбийском стиле: с добавлением карамелизованных кузнечиков.', 688.0, 1, 2),
    (3, 'Мороженое со вкусом сыра чеддер', 'Вкус настоящего сыра в вафельном стаканчике.', 501.0, 1, 4),
    (4, 'Пломбир 1937', 'Пломбир по рецепту 1937 года Московского хладокомбината.', 78.0, 2, 3),
    (5, 'Томатное мороженое', 'В СССР делали и томатное мороженое тоже. Вкус специфический.', 0.1, 2, 1);
"""

# Find wrap name with 'праздник'
cur.execute('''
SELECT ice_cream6.name,
	   wrappers6.name
FROM ice_cream6
JOIN wrappers6 ON ice_cream6.wrapper_id = wrappers6.id
WHERE wrappers6.name LIKE '%праздн%';
''')

for result in cur:
    print(result)

# Find the lowest ice_cream price
# Works only for SQL
cur.execute('''
SELECT ice_cream6.name,
	   categories6.slug,
	   wrappers6.name,
	   MIN(ice_cream6.price),
	   AVG(ice_cream6.price)
FROM ice_cream6
LEFT JOIN wrappers6 ON ice_cream6.wrapper_id = wrappers6.id
JOIN categories6 ON ice_cream6.category_id = categories6.id
GROUP BY categories6.id;
''')

for result in cur:
    print(result)

con.commit()
con.close()