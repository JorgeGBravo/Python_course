import sqlite3
from config import *

query_create_table = '''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT, surname TEXT, photo BLOB)'''
query_insert_users = '''INSERT INTO Users (name, surname, photo) VALUES (?,?,?)'''
query_select_photos = '''SELECT photo FROM Users '''
query_select_last_user = '''SELECT * FROM Users order by id desc Limit 1'''
query_select_users = '''SELECT * FROM Users'''


def view_last_user():
    con = sqlite3.connect(DB_USERS)
    user = con.execute(query_select_last_user)
    for x in user:
        return x
    con.close()


class Face:

    def __init__(self, name, surname, photo):
        self.name = name
        self.surname = surname
        self.photo = photo
        con = sqlite3.connect(DB_USERS)
        con.execute(query_create_table)
        con.execute(query_insert_users, (self.name, self.surname, self.photo))
        con.commit()
        con.close()
        view_last_user()

    @staticmethod
    def list_photos():
        con = sqlite3.connect(DB_USERS)
        return con.execute(query_select_photos)

    @staticmethod
    def list_users():
        con = sqlite3.connect(DB_USERS)
        return con.execute(query_select_users)
