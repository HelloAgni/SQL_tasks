-- You will be given a table, numbers, with one column number.
-- Return a table with a column is_even containing "Even" or "Odd" depending on number column values.

-- numbers table schema
-- number INT
-- output table schema
-- is_even STRING

-- PostgresSQL

CREATE TABLE IF NOT EXISTS numbers(
    number INT
);

INSERT INTO numbers(number)
VALUES
    (2),
    (0),
    (-7),
    (1);

SELECT number,
       CASE WHEN number % 2 = 0 THEN 'Even' ELSE 'Odd' END AS is_even
FROM numbers;
