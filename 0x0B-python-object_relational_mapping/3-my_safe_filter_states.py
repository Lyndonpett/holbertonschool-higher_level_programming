#!/usr/bin/python3
'''
This script takes an argument and lists if those values exist,
but protected from SQL injection
'''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # Connects to the database
    DB = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    # Cursor allows us to work through the database
    cur = DB.cursor()

    cur.execute("SELECT * FROM states\
    WHERE name LIKE BINARY %(name)s\
    ORDER BY states.id ASC", {'name': argv[4]})

    # Fetchall after selecting what to grab.
    states = cur.fetchall()

    # iterate through and print
    for state in states:
        print(state)

    # Close both database and cursor
    cur.close()
    DB.close()
