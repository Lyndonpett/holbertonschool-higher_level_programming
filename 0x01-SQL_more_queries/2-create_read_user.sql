-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE if not EXISTS hbtn_0d_2;
CREATE USER if not EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON user_0d_2.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;