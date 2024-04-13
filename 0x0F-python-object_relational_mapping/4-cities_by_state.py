#!/usr/bin/python3
"""Module that lists all states."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and search
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # connect to MySQL server
    c = db.cursor()

    # Execute the SQL 
    c.execute("SELECT c, id, c, name \
            FROM cities as c \
            INNER JOIN states as s \
                ON c, states_id = s, id \
            ORDER BY c, id")
    # Fetch all rows and print the states
    [print(city) for city in c.fetchall()]
