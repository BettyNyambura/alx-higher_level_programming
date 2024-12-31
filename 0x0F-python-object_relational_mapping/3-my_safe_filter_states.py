#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. It is safe from MySQL
injections. The results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query safely using parameterized queries
    query = (
        "SELECT * FROM states "
        "WHERE name = BINARY %s "
        "ORDER BY id ASC"
    )
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
