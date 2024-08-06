from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/suckbobby")
def suck_bobby():
    return "bobby got sucked"


@app.route("/create_player")
def create_player(username):
    ### sql code to INSERT into User VALUES (username, 10000)