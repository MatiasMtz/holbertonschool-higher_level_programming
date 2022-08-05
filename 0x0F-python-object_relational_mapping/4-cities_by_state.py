#!/usr/bin/python3
"""script that lists all cities with respective id and state from the database
hbtn_0e_4_usa"""

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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id=states.id \
                 ORDER BY cities.id ASC")

    # Obtaining Query Results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
