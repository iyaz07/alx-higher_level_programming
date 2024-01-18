-- List all cities in the table cities that have the state_id of california in table states in Ascending order
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
