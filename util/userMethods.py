#ruffLife
#Michelle Tang, Bo Hui Lu, Aaron Li, Kaitlin Wan
#SoftDev1 pd6
#Project 1 - ArRESTed Development

#rom flask import Flask
import sqlite3

def create():
    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    '''user info table'''
    c.execute("""CREATE TABLE IF NOT EXISTS userInfo(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                pass TEXT,
                liked_img TEXT,
                liked_words TEXT
                )"""
                )
    db.commit()
    db.close()


def checkInfo(user, pswd):

    '''This method checks if the user and password combination
    is a valid one, and returns error messages accordingly'''

    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    #Looks for the password of the inputted user
    for i in c.execute("SELECT pass FROM userInfo WHERE username = ?",(user,)):
         #If user is found and passwords match
        if i[0] == pswd:
            return "Login Successful"
         #If passwords don't match
        else:
            db.close()
            return "Incorrect Password"
    else:
        #If the user doesn't exist in the table
        db.commit()
        db.close()
        return "User not found"

def createAccount(user,pswd,passConf):

    '''This method checks the user's input when creating an acc
    to make sure they did not err anywhere in the process. If everything
    is correct, then the account will be created.'''

    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    #checks if the username already exists
    for i in c.execute("SELECT username FROM userInfo WHERE username = ?",(user,)):
        db.close()
        return "Username already exists"
    else:
        #if password confirmation fails
        if pswd != passConf:
            db.close()
            return "Passwords do not match"
        #if password confirmation succeeds add the user to the database
        userdb="INSERT INTO userInfo(username, pass, liked_img, liked_words) VALUES( ?, ?, ?, ?)"
        c.execute(userdb,(user,pswd,"liked_img_demo","liked_words_demo",))
        db.commit()
        db.close()
        return "Account creation successful"

def likedImages(user):
    '''This function returns a string of all of the url a user has liked'''
    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    c.execute("SELECT * FROM userInfo WHERE username = ?",(user,))
    url_list = c.fetchall()
    url_list= str(url_list[0][3])
    db.commit()
    db.close()
    return url_list

def addImage(user,url):
    '''This function edits an entry in the entries table'''
    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    url_list = likedImages(user)
    url_list = url_list + "," + url
    print ("URLLL HERE: \n")
    print (url_list)
    c.execute("UPDATE userInfo SET liked_img = ? WHERE username = ?",(url_list, user))
    db.commit()
    db.close()
    return 1;

def likedWords(user):
    '''This function returns a string of all of the url a user has liked'''
    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    c.execute("SELECT * FROM userInfo WHERE username = ?",(user,))
    words = c.fetchall()
    words= str(words[0][4])
    print (words)
    db.commit()
    db.close()
    return words

def addWord(user,word):
    '''This function edits an entry in the entries table'''
    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()
    words = likedWords(user)
    words = words + "," + word
    print (words)
    c.execute("UPDATE userInfo SET liked_words = ? WHERE username = ?",(words, user))
    db.commit()
    db.close()
    return 1;

def test():
    db = sqlite3.connect("../data/fluffy.db")
    c = db.cursor()

    c.execute("SELECT * FROM userInfo;")
    results = c.fetchall()
    print (results)
    db.commit()
    db.close()

create()
createAccount("user1","pass","pass")
createAccount("user2","pass","pass")
likedImages("user1")
addImage("user1", "google.com")
addImage("user1", "google2.com")
likedWords("user1")
addWord("user1", "quote1")
addWord("user2", "quote2")
test()
