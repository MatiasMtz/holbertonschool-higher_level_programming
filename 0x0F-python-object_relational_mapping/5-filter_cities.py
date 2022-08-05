#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

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
    cur.execute("SELECT cities.name FROM cities JOIN states \
                 ON cities.state_id=states.id WHERE states.name LIKE '{}' \
                 ORDER BY cities.id ASC".format(argv[4]))

    # Obtaining Query Results
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    print(", ".join(result))

    # Clean up
    cur.close()
    db.close()
