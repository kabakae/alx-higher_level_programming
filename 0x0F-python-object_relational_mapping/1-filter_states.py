#!/usr/bin/python3
"""Module that lists all states from the hbtn_Oe_O_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    #Get MySQL credentials
    #Connect to my MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve all states sorted by i.d
    c.execute("SELECT * FROM states ORDER BY id ")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
