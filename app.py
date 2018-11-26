# Team ruffLife: Xiaojie(Aaron) Li, Michelle Tang, Bo Hui Lu, Kaitlin Wan

from flask import Flask, request, render_template, session, url_for, redirect, flash

import os

# instantiate flask app
app = Flask(__name__)

# generate random key
app.secret_key = os.urandom(32)

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

@app.route("/authenticate", methods = ["POST", "GET"])
def auth():
    """
    If a user enters authenticate route manually(without logging in), redirect them back to the right road.
    If a user enters authenticate route after submitting a form:
        * if the username and password is found in the in the database, redirect to their feed
        * if username and/or the password is not found, flash an appropriate message and redirect to login
    """

    loginStatus = ''
    
    # if user got here manually, redirect to root
    if request.method == "GET" or "user" not in request.form.keys():
        return redirect('/')

    # check login creation or login
    if "pass2" in request.form.keys():
        loginStatus = auth.createAccount(request.form["user"], request.form["pass1"], request.form["pass2"])
    else:
        loginStatus = auth.checkInfo(request.form["user"], request.form["pass"])
    
    # if user successfull logs in, redirects to their feed
    if loginStatus in ["Account creation successful", "Login Successful"]:
        session["user"] = request.form["user"]
        return redirect("/feed")

@app.route("/feed")
def feed():
    return render_template("feed.html")

# run flask app with debug set to true
if __name__ == "__main__":
    app.run(debug = True)
