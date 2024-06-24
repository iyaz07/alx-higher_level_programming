#!/usr/bin/python3
"""Lists all states with name matches the argv4 protected for SQL injection"""
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
    matching_name = sys.argv[4]
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE %s "
                   "ORDER BY states.id", (matching_name,))

    info = cursor.fetchall()

    for data in info:
        print(data)

    cursor.close()
    db.close()
