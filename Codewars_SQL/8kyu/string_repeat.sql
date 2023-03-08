-- Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
-- Examples (input -> output)

-- 6, "I"     -> "IIIIII"
-- 5, "Hello" -> "HelloHelloHelloHelloHello"

-- PostgresSQL

CREATE TABLE IF NOT EXISTS repeatstr(
    id serial PRIMARY KEY,
	n INT,
    s TEXT
);
INSERT INTO repeatstr(n, s)
VALUES
    (3, '*'),
    (5, '#'),
    (2, 'ha');

SELECT s, n, REPEAT(s, n) as res
FROM repeatstr