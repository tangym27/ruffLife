from flask import Flask, render_template, request, sessions

# instantiate flask app
app = Flask(__name__)

# home, prompts user to log in if not logged in or 
# redirects to webpage if logged in
@app.route("/")
def home() :
    return;

# run flask app with debug
if __name__ == "__main__":
    app.run(debug = True)
