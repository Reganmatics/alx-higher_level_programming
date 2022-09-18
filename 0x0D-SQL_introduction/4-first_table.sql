-- create table 'first_table' if not exists with description:
-- table first_table:
-- id INT, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	PRIMARY KEY (ID)
);
