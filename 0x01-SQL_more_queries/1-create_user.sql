-- Creates a MySQL user
-- user_0d_1 gets all privileges and sets its password
CREATE USER if not EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';