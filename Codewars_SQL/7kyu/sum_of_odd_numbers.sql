-- Given the triangle of consecutive odd numbers:

--              1
--           3     5
--        7     9    11
--    13    15    17    19
-- 21    23    25    27    29

-- Calculate the sum of the numbers in the nth row of this triangle
--  (starting at index 1) e.g.: (Input --> Output)

-- 1 -->  1
-- 2 --> 3 + 5 = 8

-- PostgresSQL

CREATE TABLE IF NOT EXISTS nums(
	id serial PRIMARY KEY,
	n INT
);

INSERT INTO nums(n)
VALUES
	(1),
	(2),
	(13),
	(19),
	(41),
	(42),
	(74),
	(86),
	(93),
	(101);

SELECT CAST(POWER(n, 3) AS INT) AS res
FROM nums