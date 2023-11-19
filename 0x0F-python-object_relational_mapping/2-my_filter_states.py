#!/usr/bin/python3
"""2my filter states from hbtn_0e_0_usa database."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM states WHERE name = '{sys.argv[4]}' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
