#!/usr/bin/python3
""""""

if __name__ == "__main__":
	""""""
	from sys import argv
	import MySQLdb

	# Connecting to a MySQL database
	db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
						passwd=argv[2], db=argv[3])
	
	# Getting a Cursor in MySQL Python
	cur = db.cursor()

	# Executing MySQL Queries in Python
	cur.execute("SELECT * FROM states")

	# Obtaining Query Results
	rows = cur.fetchall()
	for row in rows:
		print(row)
	
	# Clean up
	cur.close()
	db.close()
