CREATE TABLE Devolver_digital (
Game_name VARCHAR(50),
Release_date DATE,
Metacritic_score INT
);

ALTER TABLE Devolver_digital
RENAME TO DEVOLVER_BADASS_DIGITAL;

INSERT INTO DEVOLVER_BADASS_DIGITAL
VALUES('Hotline Miami', '23-10-2012', 85);

INSERT INTO DEVOLVER_BADASS_DIGITAL
VALUES('My Friend Pedro', '20-06-2019', 81);

UPDATE DEVOLVER_BADASS_DIGITAL
SET Game_name = 'Katana Zero',
Release_date = '18-04-2019'
WHERE Metacritic_score = 85;

DELETE FROM DEVOLVER_BADASS_DIGITAL
WHERE Game_name = 'My Friend Pedro'