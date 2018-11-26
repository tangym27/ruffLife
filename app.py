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
        return redirect("/profile")
    return render_template("index.html")



# run flask app with debug
if __name__ == "__main__":
    app.run(debug = True)
