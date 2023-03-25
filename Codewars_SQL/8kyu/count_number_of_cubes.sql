-- Your function takes as parameter the number of times the cube has been cut.
-- You must return the number of smaller cubes created by
-- the cuts that have at least one red face.

-- Examples:
-- countSquares(2) --> 26
-- countSquares(4) --> 98

-- PostgresSQL

CREATE TABLE IF NOT EXISTS squares(
    id serial PRIMARY KEY,
	n INT
);
INSERT INTO squares(n)
VALUES
    (0),
    (5),
    (16),
    (23);

SELECT n,
CASE
    WHEN n = 0 THEN 1
    ELSE CAST(POWER(n + 1, 3) - POWER(n - 1, 3) AS INT)
END AS res
FROM squares