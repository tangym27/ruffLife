#ruffLife
#Michelle Tang, Bo Hui Lu, Aaron Li, Kaitlin Wan
#SoftDev1 pd6
#Project 1 - ArRESTed Development

from flask import Flask
import sqlite3


def checkInfo(user, pswd):
    
    '''This method checks if the user and password combination
    is a valid one, and returns error messages accordingly'''
    
    db = sqlite3.connect("data/fluffy.db")
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
        db.close()
        return "User not found"

    

def createAccount(user,pswd,passConf):
    
    '''This method checks the user's input when creating an acc
    to make sure they did not err anywhere in the process. If everything
    is correct, then the account will be created.'''
    
    db = sqlite3.connect("data/fluffy.db")
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
        c.execute("INSERT INTO userInfo (username,pass) VALUES(?,?)",(user,pswd,))
        db.commit()
        db.close()
        return "Account creation successful"


    
def addAnimal(url):
    
    '''This method adds the url of a animal picture that the user
    liked. It will also check to see if the user tried to add an url more
    than once, and will prevent the user from doing that.'''
    
    db = sqlite3.connect("data/fluffy.db")
    c = db.cursor()

    #checks to see if the user has already liked the animal picture
    for i in c.execute("SELECT fav_Images FROM likedImages WHERE fav_Images = ?",(url,)):
        db.close()

        return "Wow, you seem to really like this picture! Unfortunately, you've already added it before."

    #adds picture to the database
    else:

        c.execute("INSERT INTO likedImages (fav_Images) VALUES(?)",(url,))
        db.commit()
        db.close()
        return "This has been moved into your favorites."



def addWords(url):
    
    '''This method adds the url of a meme that the user
    liked. It will also check to see if the user tried to add an url more
    than once, and will prevent the user from doing that.'''
    
    db = sqlite3.connect("data/fluffy.db")
    c = db.cursor()

    #checks to see if the user has already liked the meme
    for i in c.execute("SELECT fav_Words FROM likedWords WHERE fav_Words = ?",(url,)):
        db.close()

        return "Wow, you seem to really like this meme! Unfortunately, you've already added it before."

    #adds meme to the database
    else:

        c.execute("INSERT INTO likedWords (fav_Words) VALUES(?)",(url,))
        db.commit()
        db.close()
        return "This has been moved into your favorites."
    

print(createAccount("abc","123","123")) #expect account creation successful
