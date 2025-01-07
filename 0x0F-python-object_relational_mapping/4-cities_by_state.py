#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
The argument takes 3 arguments
uses MySQLdb to connect to a MySQL
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command line arguments
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql username> "
                "<mysql password> <db name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

        # Execute the query to fetch all cities sorted by cities.id
        query = (
            """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            """
        )
        cursor.execute(query)

        # Fetch all the results
        cities = cursor.fetchall()

        # Print each city in the required format
        for city in cities:
            print(city)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()
