ALX Introduction to Structured Query Language (SQL)

Author: Stephen Ronald Nottinson

SQL provides a standard way to interact with databases and perform
various operations such as retrieving, inserting, updating, and deleting data.
SQL is used by database management systems (DBMS) like MySQL, Oracle,
Microsoft SQL Server, PostgreSQL, and SQLite. These systems provide the
software infrastructure to store, organize, and retrieve data efficiently.

Resources
Read or watch:

What is Database & SQL?
A Basic MySQL Tutorial
Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
Basic queries: SQL and RA
SQL technique: functions
SQL technique: subqueries
What makes the big difference between a backtick and an apostrophe?
MySQL Cheat Sheet
MySQL 8.0 SQL Statement Syntax
installing MySQL in Ubuntu 20.04
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc

TASKS
0. List databases
mandatory
Write a script that lists all databases of your MySQL server.
1. Create a database
mandatory
Write a script that creates the database hbtn_0c_0 in your MySQL server.
If the database hbtn_0c_0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
2. Delete a database
mandatory
Write a script that deletes the database hbtn_0c_0 in your MySQL server.
3. List tables
mandatory
Write a script that lists all the tables of a database in your MySQL server.
4. First table
mandatory
Write a script that creates a table called first_table in the current database in your MySQL server.
5. Full description
mandatory
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
6. List all in table
mandatory
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
7. First add
mandatory
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
8. Count 89
mandatory
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
9. Full creation
mandatory
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
10. List by best
mandatory
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
11. Select the best
mandatory
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
12. Cheating is bad
mandatory
Write a script that updates the score of Bob to 10 in the table second_table.
13. Score too low
mandatory
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
14. Average
mandatory
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
15. Number by score
mandatory
Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
16. Say my name
mandatory
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

AND OTHER ADVANCE TASKS
