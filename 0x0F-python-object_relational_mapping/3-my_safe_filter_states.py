#!/usr/bin/python3
"""Module that lists all states from."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Get the command
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )
    # Create a cursor
    cursor = db.cursor()
    # prepare the
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
