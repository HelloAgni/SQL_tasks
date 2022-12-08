import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# For SQLite_db and Postgres_db
"""
CREATE TABLE ice_cream2(
	is_published INTEGER,
	is_on_main INTEGER,
	name TEXT,
	text TEXT,
	category TEXT
);

INSERT INTO ice_cream2
VALUES
	(1, 1, 'Пивное мороженое', 'Со вкусом светлого нефильтрованного лагера.', 'Экзотическое'),
	(0, 1, 'Мороженое с кузнечиками', 'В колумбийском стиле: с добавлением карамелизованных кузнечиков.', 'Экзотическое'),
	(0, 0, 'Мороженое со вкусом сыра чеддер', 'Вкус настоящего сыра в вафельном стаканчике.', 'Экзотическое'),
	(1, 0, 'Пломбир 1937', 'Пломбир по рецепту 1937 года Московского хладокомбината.', 'Обычное'),
	(1, 1, 'Томатное мороженое', 'В СССР делали и томатное мороженое тоже. Вкус специфический.', 'Обычное');
"""

# name, text; is_published True, Limit 2, OFFSET
cur.execute('''
SELECT name,
       text
FROM ice_cream2
WHERE is_published=1
ORDER BY name DESC
LIMIT 2 OFFSET 1;
''')

for result in cur:
    print(result)

con.commit()
con.close()