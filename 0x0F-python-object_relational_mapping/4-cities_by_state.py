#!/usr/bin/python3
"""Lists all cities name in the MySQL"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "INNER JOIN states ON states.id=cities.state_id "
                   "ORDER BY cities.id")

    info = cursor.fetchall()

    for data in info:
        print(data)

    cursor.close()
    db.close()
