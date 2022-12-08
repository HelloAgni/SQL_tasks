import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# For SQLite_db and Postgres_db
"""
CREATE TABLE ice_cream1(
    is_published INTEGER,
    is_on_main INTEGER,
    name TEXT,
    text TEXT,
    category TEXT,
    price REAL
);
INSERT INTO ice_cream1
VALUES
    (1, 1, 'Пивное мороженое', 'Со вкусом светлого нефильтрованного лагера.', 'Экзотическое', 500),
    (0, 1, 'Мороженое с кузнечиками', 'В колумбийском стиле: с добавлением карамелизованных кузнечиков.', 'Экзотическое', 688),
    (0, 0, 'Мороженое со вкусом сыра чеддер', 'Вкус настоящего сыра в вафельном стаканчике.', 'Экзотическое', 500),
    (1, 0, 'Пломбир 1937', 'Пломбир по рецепту 1937 года Московского хладокомбината.', 'Обычное', 78),
    (1, 1, 'Томатное мороженое', 'В СССР делали и томатное мороженое тоже. Вкус специфический.', 'Обычное', 0.1);
"""

# MIN price
cur.execute('''
SELECT MIN(price)
FROM ice_cream1;
''')
for result in cur:
    print(result)

# AVG(price) WHERE category = 'Экзотическое'
cur.execute('''
SELECT AVG(price)
FROM ice_cream1
WHERE category = 'Экзотическое';
''')
for result in cur:
    print(result)

# COUNT TRUE is_published and is_on_main
cur.execute('''
SELECT SUM(price)
FROM ice_cream1
WHERE is_published = 1 AND is_on_main = 1;
''')
for result in cur:
    print(result)

con.commit()
con.close()