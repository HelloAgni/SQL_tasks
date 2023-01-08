import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS toppings7(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream7(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream_toppings7(
id INTEGER PRIMARY KEY,
ice_cream_id INTEGER NOT NULL,
topping_id INTEGER NOT NULL,
FOREIGN KEY(ice_cream_id) REFERENCES ice_cream7(id),
FOREIGN KEY(topping_id) REFERENCES toppings7(id)
);
''')

con.commit()
con.close()