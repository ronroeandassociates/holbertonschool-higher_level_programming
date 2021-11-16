#!/usr/bin/python3
"""Module lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
    
    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=password,
                         db=database,
                         port=3306)
    
    cur = db.cursor()
    
    cur.execute("SELECT id, name FROM states ORDER BY ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
