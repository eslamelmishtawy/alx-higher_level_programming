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

    sql = f"SELECT * FROM states
          WHERE name = str({sys.argv[4]})
          ORDER BY id ASC"

    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
