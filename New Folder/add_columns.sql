ALTER TABLE hon
ADD COLUMN rel Float,
ADD COLUMN cal INTEGER,

ALTER TABLE hon
DROP COLUMN rel,
DROP COLUMN cal,


SELECT * FROM hon
