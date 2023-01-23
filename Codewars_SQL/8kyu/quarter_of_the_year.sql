-- Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
-- For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

-- Constraint:
-- 1 <= month <= 12

-- PostgresSQL

CREATE TABLE IF NOT EXISTS quarterof(
    id serial PRIMARY KEY,
	month INT
);
-- INSERT INTO quarterof(month)
-- SELECT *
-- FROM unnest(ARRAY[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
INSERT INTO quarterof(month)
SELECT unnest(ARRAY[generate_series(1,12)]);

-- V1
-- SELECT month,
-- 	   CAST(CEIL(CAST(month AS FLOAT)/ 3) AS INT) AS res
-- FROM quarterof;

-- V2
SELECT month,
      (CEIL(month / 3.0))::int AS res
FROM quarterof

-- V3
-- SELECT month, CAST(CEILING(month / 3.0) AS INT) AS res 
-- FROM quarterof