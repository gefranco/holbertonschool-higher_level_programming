#!/usr/bin/python3
'''
displays all values in the states table of hbtn_0e_0_usa according the argument
'''
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states where name = '{}'".format(sys.argv[4])
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
