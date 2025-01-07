#!/usr/bin/python3
"""
This script lists all cities of a given state from thr db.

It takes 4 arguments:
Results are sorted in ascending order by `cities.id`

The script uses MySQLdb to connect to a MySQL server.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command line arguments
    if len(sys.argv) != 5:
        print("Usage: ./script.py <user> <password> <database> <state>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to fetch all cities of the given state
        query = (
            "SELECT cities.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC;"
        )
        cursor.execute(query, (state_name,))

        # Fetch all the results
        cities = cursor.fetchall()

        # Print cities as a comma-separated list
        print(", ".join(city[0] for city in cities))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
