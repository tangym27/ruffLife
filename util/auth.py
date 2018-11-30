from flask import Flask
import sqlite3


'''This method checks if the user and password combination
is a valid one, and returns error messages accordingly'''
def checkInfo(user, pswd):
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

    

    '''This method checks the user's input when creating an acc
to make sure they did not err anywhere in the process. If everything
is correct, then the account will be created.'''
def createAccount(user,pswd,passConf):
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


    
'''This method adds the url of a animal picture that the user
liked. It will also check to see if the user tried to add an url more
than once, and will prevent the user from doing that.'''
def addAnimal(url):
    db = sqlite3.connect("data/fluffy.db")
    c = db.cursor()

    #checks to see if the user has already liked the animal picture
    for i in c.execute("SELECT fav_Animal FROM userInfo WHERE fav_Animal = ?",(url,)):
        db.close()

        return "Wow, you seem to really like this picture! Unfortunately, you've already added it before."

    #adds picture to the database
    else:

        c.execute("INSERT INTO userInfo (fav_Animal) VALUES(?)",(url,))
        db.commit()
        db.close()
        return "This has been moved into your favorites."


    '''This method adds the url of a meme that the user
liked. It will also check to see if the user tried to add an url more
than once, and will prevent the user from doing that.'''
def addMeme(url):
    db = sqlite3.connect("data/fluffy.db")
    c = db.cursor()

    #checks to see if the user has already liked the meme
    for i in c.execute("SELECT fav_Meme FROM userInfo WHERE fav_Meme = ?",(url,)):
        db.close()

        return "Wow, you seem to really like this meme! Unfortunately, you've already added it before."

    #adds meme to the database
    else:

        c.execute("INSERT INTO userInfo (fav_Meme) VALUES(?)",(url,))
        db.commit()
        db.close()
        return "This has been moved into your favorites."
    

print(createAccount("abc","123","123")) #expect account creation successful
