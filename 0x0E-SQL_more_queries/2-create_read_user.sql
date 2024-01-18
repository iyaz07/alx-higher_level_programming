--  This script creates database v and grantes user_0d_2 SELECT 
--  The user_0d_2 password should be set to user_0d_2_pwd
--  If the database hbtn_0d_2 already exists, your script should not fail
--  If the user user_0d_2 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
