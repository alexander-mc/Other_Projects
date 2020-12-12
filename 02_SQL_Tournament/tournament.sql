-- Start clean with a new database

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- Create tables, 'players' and 'matches'

CREATE TABLE Players (
	Player_ID serial primary key,
	Player_Name text);


CREATE TABLE Matches (
	Match_ID serial primary key,
--	Round integer,
	Won integer references Players (Player_ID),
	Lost integer references Players (Player_ID));


-- Insert into table 'players' test valeus

-- INSERT INTO Players (Player_Name) VALUES ('A');
-- INSERT INTO Players (Player_Name) VALUES ('B');
-- INSERT INTO Players (Player_Name) VALUES ('B');
-- INSERT INTO Players (Player_Name) VALUES ('C');
-- INSERT INTO Players (Player_Name) VALUES ('D');
-- INSERT INTO Players (Player_Name) VALUES ('E');


-- Input into table 'matches' test values

-- INSERT INTO Matches (Won, Lost) VALUES (1,2);
-- INSERT INTO Matches (Won, Lost) VALUES (3,4);
-- INSERT INTO Matches (Won, Lost) VALUES (6,5);
-- INSERT INTO Matches (Won, Lost) VALUES (1,3);
-- INSERT INTO Matches (Won, Lost) VALUES (4,2);
-- INSERT INTO Matches (Won, Lost) VALUES (6,5);


-- Scratch

-- CREATE TABLE Results (
--	Match_ID serial references Matches (Match_ID),
--	Player_ID integer references Players (Player_ID),
--	Player_Name text,
--	Result text,
--	Points integer);

