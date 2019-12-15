#!/usr/bin/python3
'''
script that lists all states with a name starting with N from hbtn_0e_0_usa
'''
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cur = db.cursor()

    cur.execute("""SELECT * FROM states where name LIKE BINARY 'N%'""")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
