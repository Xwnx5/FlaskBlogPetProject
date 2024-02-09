import math
import time
import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = """SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Error db reading')
        return []
    
    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error adding post in db' + str(e))
            return False
        return True
    
    def getPost(self, postId):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE id = {postId} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Error getting post from db' + str(e))
        return (False, False)
    
    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print('Error getting post from db' + str(e))
        return []