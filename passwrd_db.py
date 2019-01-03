import sqlite3
import sys
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        print("Database Opened")
        return conn
    except Error as e:
        print(e)
    return None

def add_site(conn,site, user, password):
    cur = conn.cursor()
    sql = '''INSERT INTO Sites(site, user, password)
                VALUES(?, ?, ?) '''
    data = (site, user, password)
    cur.execute(sql, data)
    return cur.lastrowid
def select_all(conn):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Sites''')
    rows = cur.fetchall()
    for row in rows:
        print( row)

def main():
    database = "password.db"
    connection = create_connection(database)
    with connection:
        while True:
            print("Welcome to Password Database")
            command = str(input("Select CMD (SELECT, CREATE, QUIT)"))
            if command == "SELECT":
                select_all(connection)
            elif command == "CREATE":
                site = str(input("site name"))
                user = str(input("username"))
                password = str(input("password"))
                add_site(connection, site, user, password)
            elif command == "QUIT":
                sys.exit()
            else:
                print("Incorrect Command")
if __name__ == '__main__':
    main()
