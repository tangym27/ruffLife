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
            pass TEXT
            )"""
            )

'''user's liked images(animals, memes) table'''
c.execute("""CREATE TABLE IF NOT EXISTS likedImages(
username TEXT UNIQUE,
fav_Images TEXT,
)"""
)

'''user's liked quotes table'''
c.execute("""CREATE TABLE IF NOT EXISTS likedWords(
username TEXT UNIQUE,
fav_Words TEXT)"""
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
