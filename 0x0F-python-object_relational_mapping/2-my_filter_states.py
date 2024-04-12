#!/usr/bin/python3

"""Module that lists all states."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL.credential
    # and connect to 
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL
    c.execute("SELECT * \
            FROM states \
            WHERE BINARY name = '{}'".formart(sys.argv[4]))
    # Fetch all 
    [print(state) for state in c.fetchall()]
