# Team ruffLife: Xiaojie(Aaron) Li, Michelle Tang, Bo Hui Lu, Kaitlin Wan
# SoftDev1 pd6
# P#01 -- arRESTed Development
# 2018-11-30

import os
import json
import urllib


from util import userMethods

from flask import Flask, request, render_template, session, url_for, redirect, flash

# instantiate flask app
app = Flask(__name__)

# generate random key
app.secret_key = os.urandom(32)
username = ""

# root route
@app.route("/")
def home():
    """
    If user is logged in, redirect them to their feed.
    If not logged in, prompt login page
    """

    if "user" in session:
        print(request.form("user"))
        return redirect("/feed")

    return render_template("index.html")

    # authentication route
@app.route("/authenticate", methods = ["POST", "GET"])
def authenticate():
    """
    If a user enters authenticate route manually(without logging in), redirect them back to the right road.
    If a user enters authenticate route after submitting a form:
        * if the username and password is found in the in the database, redirect to their feed
        * if username and/or the password is not found, flash an appropriate message and redirect to login
    """

    loginStatus = ''
    global username

    # if user got here manually, redirect to root
    if request.method == "GET" or "user" not in request.form.keys():
        return redirect('/')

    # check login creation or login
    if "pass2" in request.form.keys():
        print("\n\nCREATING ACCOUNT\n")
        loginStatus = userMethods.createAccount(request.form["user"], request.form["pass1"], request.form["pass2"])
    else:
        print("\n\nCHECKING INFO\n")
        loginStatus = userMethods.checkInfo(request.form["user"], request.form["pass"])

    # if user successfull logs in, redirects to their feed
    if loginStatus == "Account creation successful":
        session["user"] = request.form["user"]
        username = request.form["user"]
        print("\n\n-------\n" + username + "\n")
        flash(loginStatus + ". To see your personal feed, login above.")
        return render_template("index.html")
    elif loginStatus == "Login Successful":
        username = request.form["user"]
        print("\n\n---Login SUccessful----\n" + username + "\n")
        session["user"] = request.form["user"]
        flash(loginStatus)
        return redirect("/feed")
    else:
        flash(loginStatus)
        return redirect("/")

# for logged in users: their complete page
@app.route("/feed")
def feed():
    # if user not logged in redirect them
    if not("user" in session):
        flash("You are not logged in.")
        return redirect("/")

    url = "https://random.dog/woof.json"
    status = True;
    while(status):
        straw = urllib.request.urlopen(url)
        straw = straw.read()
        dict = json.loads(straw)
        print(dict["url"][-3:])
        if(dict["url"][-3:] != "mp4"):
            status = False

    url = "https://aws.random.cat/meow"
    straw = urllib.request.urlopen(url)
    straw = straw.read()
    cat = json.loads(straw)

    url = "https://catfact.ninja/fact"
    straw = urllib.request.urlopen(url)
    straw = straw.read()
    cat_fact = json.loads(straw)
    print(cat_fact['fact'])

    url = urllib.request.urlopen("https://favqs.com/api/qotd")
    data = json.loads(url.read().decode())
    data = data["quote"]
    print(data["body"])
    print("\n-------------------\n" + username + "\n----------------------\n")
    # otherwise, load the feed
    return render_template("feed.html", dog_link = dict['url'], cat_link = cat["file"], cat_fact = cat_fact["fact"], quote = data["body"], author = data["author"], user = username)

@app.route("/reload", methods=["GET", "POST"])
def reload():
    if not ("user" in session):
        flash("You are not logged in.")
        return redirect("/")
    if request.method == "POST":
        return redirect("/feed#doge")
    else:
        return redirect("/feed#cat")

# logout route
@app.route("/logout")
def logout():
    # pop user from session and redirect to login page(root)
    if "user" in session:
        session.pop("user")
        flash("You have been logged out successfully!")
    return redirect("/")

@app.route("/signup")
def signup():
    # otherwise, load the feed
    return render_template("signup.html")

@app.route("/home")
def homeee():
    # otherwise, load the feed
    return redirect("/")

@app.route("/feed")
def logginnn():
    # otherwise, load the feed
    return render_template("feed.html")

@app.route("/weather")
def weather():
    # otherwise, load the feed
    return render_template("weather.html")

@app.route("/quote")
def quote():
    # otherwise, load the feed
    url = 'https://favqs.com/api/qotd'
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    flash("LOG IN TO LIKE ITEMS!!")
    return render_template("quote.html", link = d['quote']['body'], auth = d['quote']["author"] )

@app.route("/catpic")
def catpic():
    url = "https://aws.random.cat/meow"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    flash("LOG IN TO LIKE ITEMS!!")
    # otherwise, load the feed
    return render_template("catpic.html", link = d['file'])

@app.route("/dogpic")
def dogpic():
    url = "https://random.dog/woof.json"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    # otherwise, load the feed
    return render_template("dogpic.html", link = d['url'])

@app.route("/fact")
def fact():
    # otherwise, load the feed
    return render_template("fact.html")

@app.route("/meme")
def meme():
    # otherwise, load the feed
    return render_template("meme.html")

@app.route("/like")
def like():
    #TEMPORAY PLACEHOLDER LINK
    return render_template("feed.html")


# run flask app with debug set to true
if __name__ == "__main__":
    app.run(debug = True)
