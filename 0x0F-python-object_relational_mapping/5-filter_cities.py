#!/usr/bin/python3
"""Lists all cities in a specific city in the MySQL"""
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
    state_search = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities "
                   "INNER JOIN states ON states.id=cities.state_id "
                   "WHERE states.name=%s"
                   "ORDER BY cities.id", (state_search,))

    info = cursor.fetchall()

    list_info = [data[0] for data in info]

    print(", ".join(list_info))
    cursor.close()
    db.close()
