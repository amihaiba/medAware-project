-- Create the database, user and a table for the app to insert records into
CREATE DATABASE IF NOT EXISTS med_db;
CREATE USER IF NOT EXISTS 'med_user'@'%' IDENTIFIED BY 'med_pass';
GRANT ALL PRIVILEGES ON med_db.* TO 'med_user'@'%';
FLUSH PRIVILEGES;
USE med_db;
CREATE TABLE IF NOT EXISTS med_records
(
    file_name VARCHAR(30) PRIMARY KEY,
    file_content TEXT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);