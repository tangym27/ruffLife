#ruffLife
#Michelle Tang, Bo Hui Lu, Aaron Li, Kaitlin Wan
#SoftDev1 pd6
#Project 1 - ArRESTed Development

import sqlite3

db = sqlite3.connect("../data/fluffy.db")

c = db.cursor()

'''user info table'''
c.execute("""CREATE TABLE IF NOT EXISTS userInfo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            pass TEXT,
            fav_Animal TEXT,
            fav_Meme TEXT)"""
            )

'''user's likes table'''
c.execute("""fav_Animal TEXT,
fav_Meme TEXT)"""
)


'''quotes table'''
c.execute("""CREATE TABLE IF NOT EXISTS quotes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT)"""
            )

'''weather table'''
c.execute("""CREATE TABLE IF NOT EXISTS weather(
            day TEXT PRIMARY KEY,
            temp TEXT,
            condition TEXT)"""
            )

db.commit()
db.close()
