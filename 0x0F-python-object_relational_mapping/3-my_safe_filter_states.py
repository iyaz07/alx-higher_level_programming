#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where
name matches argv(4)
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and fetch row(s) or column(s)
    """
    # Check if the number of arguments is correct
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Start cursor
    cur = db.cursor()

    # Query using parameterized value to avoid injection
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()

    # Print query
    for row in rows:
        print(row)

    # Close cursor
    cur.close()
    db.close()
