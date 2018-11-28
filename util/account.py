#ruffLife
#Michelle Tang, Bo Hui Lu, Aaron Li, Kaitlin Wan
#SoftDev1 pd6
#Project 1 - ArRESTed Development


import flask import Flask
import sqlite3

def accCreator(user, pswd, confirmPswd)
    
    '''This method takes in three arguments, which are the user, password, and 
    the confirmation password. This checks to see if account exists and will stop
    it from being made if that is the case. It will also check if the user's 
    inputted confirmation password matches the password they inputted, to make 
    sure their password is what they want it to be.'''

    db = sqlite3.connect("data/fluffy.db")
    c = db.cursor()

    #does account exist?
    for i in c.execute("SELECT username FROM userinfo WHERE username = ?", (user,)):
        db.close()
        return "Aww shucks, your username is taken already! You should go find and 
marry that person, you two must have great compatiblity"


    #now,does the password match?
    else:

        #passwords DO NOT match
        if pswd != confirmPswd:
            db.close()
            return "Whoopsies, your passwords don't match"

        
        #passwords DO match
        c.execute("INSERT INTO userInfo (username, pass) Values(?,?)", (user,pswd,))
        db.commit()
        db.close()
        return "You did it! Welcome to this amazing website"


    

def confirmInfo(user,pswd):

    '''This method will take the two arguments(username, password) and check
    to see if the inputted data matches what we have in our database. It will
    return an appropriate error msg if it doesn't succeed.'''

    db = sqlite3.connect("data/fluffy.db")
    c = db.cursor()

    #seaches for password of inputted user
    for i in c.execute("SELECT pass from userInfo WHERE username = ?", (user,)):

        #if user exiss and password also matches
        if i[0] == pswd:
            return "You did it!"

        #password does not match
        else:
            db.close()
            return "Sorry, your password is not right"

    #user cannot be found in table
    else:
        db.close()
        return "Sorry, your username cannot be found"

    
