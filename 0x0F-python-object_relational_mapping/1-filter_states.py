#!/usr/bin/python3

"""
list all states
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
            where name like binary 'N%' ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
