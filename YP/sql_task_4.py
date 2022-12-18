import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# For SQLite_db and Postgres_db
"""
CREATE TABLE IF NOT EXISTS wrappers(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT,
wrapper_id INTEGER UNIQUE,
FOREIGN KEY(wrapper_id) REFERENCES wrappers(id)
);

INSERT INTO wrappers
VALUES
(1, 'Бумажная с черепами');

INSERT INTO ice_cream(id, name, description)
VALUES
(1, 'Пивное мороженое', 'Со вкусом светлого нефильтрованного лагера.'),
(2, 'Мороженое с кузнечиками', 'В колумбийском стиле: с добавлением карамелизованных кузнечиков.'),
(3, 'Мороженое со вкусом сыра чеддер', 'Вкус настоящего сыра в вафельном стаканчике.'),
(4, 'Пломбир 1937', 'Пломбир по рецепту 1937 года Московского хладокомбината.');
INSERT INTO ice_cream
VALUES
(5, 'Томатное мороженое', 'В СССР делали и томатное мороженое тоже. Вкус специфический.', 1);
"""

# ice.name and wrapper.name
cur.execute('''
SELECT ice_cream.name,
       wrappers.name
FROM ice_cream,
     wrappers
WHERE ice_cream.wrapper_id = wrappers.id AND
      wrappers.name = 'Бумажная с черепами';
''')

for result in cur:
    print(result)

con.commit()
con.close()