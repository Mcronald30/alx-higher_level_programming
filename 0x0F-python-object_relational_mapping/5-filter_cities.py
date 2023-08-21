#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", (sys.argv[4],))
    results = cur.fetchall()
    city_names = ", ".join(result[0] for result in results)
    print(city_names)
    cur.close()
    db.close()
