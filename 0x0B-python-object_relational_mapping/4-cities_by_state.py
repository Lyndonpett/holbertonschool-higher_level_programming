#!/usr/bin/python3
'''This script lists all cities from a Database'''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # Connects to the database
    DB = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    # Cursor allows us to work through the database
    cur = DB.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM\
    cities INNER JOIN states ON cities.state_id = states.id;")

    # Fetchall after selecting what to grab.
    cities = cur.fetchall()

    # iterate through and print
    for city in cities:
        print(city)

    # Close both database and cursor
    cur.close()
    DB.close()
