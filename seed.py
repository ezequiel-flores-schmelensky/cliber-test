import sqlite3
import requests


def saveUsers( cursor, sqliteConnection, total=150):
    print("total: " + str(total))
    since = 0
    sqlite_insert_query = "INSERT INTO users (id, username, image_url, type, link) VALUES "
    while (total>0):
        per_page = 100 if total > 100 else total
        url = "https://api.github.com/users?since=" + str(since) + "&per_page=" + str(per_page) #100max 
        users = requests.get(url = url, headers = {"Accept": "application/vnd.github.v3+json"} )
        usersJSON = users.json()
        
        if since > 0:
            sqlite_insert_query += ","

        for user in usersJSON:
            sqlite_insert_query += ("(" + str(user["id"]) + 
                                    ", '" + user["login"] + 
                                    "', '" + user["avatar_url"] + 
                                    "', '" + user["type"] + 
                                    "', '" + user["html_url"] + "'),")

        lastC = len(sqlite_insert_query)
        sqlite_insert_query = sqlite_insert_query[:(lastC-1)]
        last = len(usersJSON) - 1
        since = usersJSON[last]["id"]
        total = total-100 if total > 100 else total-total

    print(sqlite_insert_query)
    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    sqlite_select_query = """SELECT count(*) from users"""
    cursor.execute(sqlite_select_query)
    totalRows = cursor.fetchone()
    print("Total rows are:  ", totalRows)

try:
    sqliteConnection = sqlite3.connect('cliber.db')
    
    cursor = sqliteConnection.cursor()
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
    if cursor.fetchone()[0]==1:
        print('Table exists.')
        cursor.execute('''DROP TABLE users''')
        sqliteConnection.commit()

    sqlite_create_table_query = '''CREATE TABLE users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            image_url TEXT NOT NULL,
                            type TEXT NOT NULL,
                            link TEXT NOT NULL);'''
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()

    print("Introduce a total of users")
    total = input()
    totalAux = int(total) if total != '' else 150
    saveUsers(cursor, sqliteConnection, totalAux)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")


