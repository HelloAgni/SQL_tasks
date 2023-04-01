-- In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
-- you need to return the other complementary side.

-- Example: (input --> output)
-- "ATTGC" --> "TAACG"
-- "GTAT" --> "CATA"

-- PostgresSQL

CREATE TABLE IF NOT EXISTS dnastrand(
    id serial PRIMARY KEY,
    dna TEXT
);
INSERT INTO dnastrand(dna)
VALUES
	('AAAA'),
	('ATTGC'),
	('GTAT'),
	('AAGG'),
	('CGCG'),
	('ATTGC'),
	('GTATCGATCGATCGATC');

SELECT dna, TRANSLATE(dna,'ACGT','TGCA') AS res
FROM dnastrand