-- Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
-- You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

-- For example:
-- hours = 3 ----> liters = 1
-- hours = 6.7---> liters = 3
-- hours = 11.8--> liters = 5

-- You have to return 3 columns: id, hours and liters (not litres, it's a difference from the kata description)

-- PostgresSQL

CREATE TABLE cycling(
    id serial PRIMARY KEY,
	hours DECIMAL(9,2)
);

INSERT INTO cycling(hours)
VALUES 
    (68.92),
    (63.3),
    (66.41),
    (70.59),
    (53.68);

SELECT *, FLOOR(hours / 2) AS liters
FROM cycling;