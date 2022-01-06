#!/usr/bin/python3
'''This script lists a given city from a Database'''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # Connects to the database
    DB = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    # Cursor allows us to work through the database
    cur = DB.cursor()

    cur.execute("SELECT cities.name FROM\
    cities INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name LIKE BINARY %(name)s\
    ORDER BY cities.id ASC", {'name': argv[4]})

    # Fetchall after selecting what to grab.
    cities = cur.fetchall()

    # iterate through and print
    for i, city in enumerate(cities, start=0):
        if i != 0:
            print(", ", end="")
        print(city[0], end="")
    print("")

    # Close both database and cursor
    cur.close()
    DB.close()
