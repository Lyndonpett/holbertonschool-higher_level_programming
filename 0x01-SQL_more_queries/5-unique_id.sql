-- creates the table unique_id on your MySQL server
CREATE TABLE if not EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));