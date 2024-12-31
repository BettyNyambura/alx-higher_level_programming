#!/usr/bin/python3
"""
Lists all states with a name starting with N from the db hbtn_0e_0_usa.
The results are sorted in ascending order using state.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Execute the query
    cursor.execute(
            "SELECT * FROM states"
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC"
    )

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
