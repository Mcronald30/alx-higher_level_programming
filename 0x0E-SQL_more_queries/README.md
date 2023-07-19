0x0E. SQL - More queries

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create a new MySQL user
How to manage privileges for a user to a database or table
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION

Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
In the container, credentials are root/root

How to import a SQL dump
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

Tasks
0. My privileges!
mandatory
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
1. Root user
mandatory
Write a script that creates the MySQL server user user_0d_1.
2. Read user
mandatory
Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
3. Always a name
mandatory
Write a script that creates the table force_name on your MySQL server.
4. ID can't be null
mandatory
Write a script that creates the table id_not_null on your MySQL server.
5. Unique ID
mandatory
Write a script that creates the table unique_id on your MySQL server.
6. States table
mandatory
Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
7. Cities table
mandatory
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
8. Cities of California
mandatory
Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
9. Cities by States
mandatory
Write a script that lists all cities contained in the database hbtn_0d_usa.
10. Genre ID by show
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download

Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
11. Genre ID for all shows
mandatory
Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)

Write a script that lists all shows contained in the database hbtn_0d_tvshows.
12. No genre
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)

Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
13. Number of shows by genre
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
14. My genres
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)

Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
15. Only Comedy
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)

Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

The tv_genres table contains only one record where name = Comedy (but the id can be different)
16. List shows and genres
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)

Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
