#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. Safe from MySql
injections."""

if __name__ == "__main__":
    """Access to db and get the values"""
    from sys import argv
    import MySQLdb

    # Connecting to a MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Getting a Cursor in MySQL Python
    cur = db.cursor()

    # Executing MySQL Queries in Python
    cur.execute("SELECT * FROM states WHERE name=%s \
                 ORDER BY states.id ASC", [argv[4]])

    # Obtaining Query Results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
