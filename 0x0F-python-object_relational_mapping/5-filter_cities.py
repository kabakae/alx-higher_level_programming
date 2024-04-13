#!/usr/bin/python3

"""Module that lists all states from."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query
    query = ("SELECT * FROM cities as c \
            INNER JOIN states as s \
            ON c . state_id = s . id \
            ORDER BY c .id ")
    c.execute(query)
    # Fetch all rows
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
