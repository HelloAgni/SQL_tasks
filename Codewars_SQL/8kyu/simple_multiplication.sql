-- This kata is about multiplying a given number
-- by eight if it is an even number and by nine otherwise.

-- PostgresSQL

CREATE TABLE IF NOT exists multiplication(
	id serial PRIMARY KEY,
	number INT
);

INSERT INTO multiplication(number)
VALUES
	(2),
	(1),
	(8),
	(4),
	(5);
	
SELECT number,
CASE
    WHEN number % 2 = 0 THEN number * 8
    ELSE number * 9
END AS res
FROM multiplication