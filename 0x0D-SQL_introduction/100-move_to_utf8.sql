-- Change database to utf-8
-- Use hbtn_0c_0 database
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Changing table in the database
USE hbtn_0c_0;
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
