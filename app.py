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
flashMessage = ""

# root route
@app.route("/")
def home():
    """
    If user is logged in, redirect them to their feed.
    If not logged in, prompt login page
    """
    if "user" in session:
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
        flash(loginStatus + ". To see your personal feed, login above.")
        return render_template("index.html")
    elif loginStatus == "Login Successful":
        session["user"] = request.form["user"]
        username = request.form["user"]
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

    api = "SRjFBkxPqxKoBspQ2HdwQxt4wsDnbArq"
    url = "http://api.giphy.com/v1/gifs/random?api_key=SRjFBkxPqxKoBspQ2HdwQxt4wsDnbArq&tag=meme&rating=pg"
    straw = urllib.request.urlopen(url)
    straw = straw.read()
    memes = json.loads(straw)
    print(memes['data']['url'])

    url = "http://randomuselessfact.appspot.com/random.json?language=en"
    straw = urllib.request.urlopen(url)
    straw = straw.read()
    facts = json.loads(straw)
    print(facts["text"])

    # otherwise, load the feed
    return render_template("feed.html", dog_link = dict['url'], cat_link = cat["file"], quote = data["body"], author = data["author"], user = username, link = memes['data']['url'], em = memes['data']['embed_url'], fact = facts["text"], )

@app.route("/reload", methods=["GET", "POST"])
def reload():
    if not ("user" in session):
        flash("You are not logged in.")
        return redirect("/")
    if request.method == "POST":
        return redirect("/feed#doge")
    else:
        return redirect("/feed#cat")

@app.route("/reload2", methods=["GET", "POST"])
def reload2():
    if not ("user" in session):
        flash("You are not logged in.")
        return redirect("/")
    if request.method == "POST":
        return redirect("/feed#fact")
    else:
        return redirect("/feed#quote")

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
    global flashMessage
    global username
    global liked
    global liked_a
    # otherwise, load the feed
    url = 'https://favqs.com/api/qotd'
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    session.pop('_flashes', None)
    flashMessage = "TO LIKE QUOTE, PLEASE LOG IN!!"
    #flash(flashMessage)
    liked = d['quote']['body']
    liked_a = d['quote']["author"]
    return render_template("quote.html", link = d['quote']['body'], auth = d['quote']["author"] )

@app.route("/add_quote")
def add_quote():
    global liked
    global liked_a
    global username
    userMethods.addWord(username, liked)
    return render_template("quote.html", link = liked, auth = liked_a)

@app.route("/catpic")
def catpic():
    global flashMessage
    global username
    global liked
    url = "https://aws.random.cat/meow"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    session.pop('_flashes', None)
    print("USERNAME")
    print (username)
    liked = d['file']
    flashMessage = "TO LIKE PHOTO, PLEASE LOG IN!!"
    #flash(flashMessage)
    # otherwise, load the feed
    return render_template("catpic.html", link = d['file'])

@app.route("/add_cat")
def add_cat():
    global liked
    global username
    userMethods.addImage(username, liked)
    return render_template("catpic.html", link = liked)

@app.route("/dogpic")
def dogpic():
    global username
    global liked
    url = "https://random.dog/woof.json"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    session.pop('_flashes', None)
    liked = d['url']

    flashMessage = "TO LIKE PHOTO, PLEASE LOG IN!!"
    #flash(flashMessage)
    # otherwise, load the feed
    return render_template("dogpic.html", link = d['url'])

@app.route("/add_dog")
def add_dog():
    global liked
    global username
    userMethods.addImage(username, liked)
    return render_template("dogpic.html", link = liked)

@app.route("/fact")
def fact():
    global username
    global liked
    url = "http://randomuselessfact.appspot.com/random.json?language=en"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    session.pop('_flashes', None)
    flashMessage = "TO LIKE FACT, PLEASE LOG IN!!"
    #flash(flashMessage)
    liked = d['text']
    print("dfadsfds")
    print (liked)
    # otherwise, load the feed
    return render_template("fact.html", link = d['text'])

@app.route("/add_fact")
def add_fact():
    global liked
    global username
    print(liked)
    userMethods.addWord(username, liked)
    return render_template("fact.html", link = liked)

@app.route("/meme")
def meme():
    global flashMessage
    f = open("./api/meme.txt", "r")
    mykey = f.readline().strip()
    api = "SRjFBkxPqxKoBspQ2HdwQxt4wsDnbArq"
    url = "http://api.giphy.com/v1/gifs/random?api_key=" + mykey + "&tag=meme&rating=pg"
    print(url)
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    print(d['data']['url'])
    session.pop('_flashes', None)
    flashMessage = "TO LIKE GIF, PLEASE LOG IN!!"
    #flash(flashMessage)
    # otherwise, load the feed
    return render_template("meme.html",link = d['data']['url'], em = d['data']['embed_url'])

# @app.route("/add_meme")
# def add_meme():
#     global liked
#     global username
#     userMethods.addImage(username, liked)
#     return render_template("dogpic.html", link = liked)
# @app.route("/like")
# def like():
#     #TEMPORAY PLACEHOLDER LINK
#     return render_template("feed.html")


# run flask app with debug set to true
if __name__ == "__main__":
    app.run(debug = True)
