-- Given a year, return the century it is in.

-- Examples
-- 1705 --> 18
-- 1900 --> 19
-- 1601 --> 17
-- 2000 --> 20

-- PostgresSQL

CREATE TABLE IF NOT EXISTS years(
	id serial PRIMARY KEY,
	yr INT
);

INSERT INTO years(yr)
VALUES
	(1705),
	(1900),
	(1601),
	(2000),
	(356),
	(89);

SELECT
CASE
    WHEN yr % 100 = 0 THEN yr / 100
    ELSE yr / 100 + 1
END AS century
FROM years