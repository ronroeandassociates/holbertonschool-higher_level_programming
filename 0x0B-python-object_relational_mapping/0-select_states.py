"""Module lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

# default values user="root", passwd="", db="hbtn_0e_0_usa"
db = MySQLdb.connect(host="localhost",
                      port=3306,
                      user=argv[1],
                      passwd=argv[2],
                      db=argv[3])
 cur = db.cursor()
  cur.execute("SELECT * FROM states ORDER BY states.id ASC")

   for row in cur.fetchall():
        print(row)
    db.close()


if __name__ == "__main__":
    main()
