from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/suckbobby")
def suck_bobby():
    return "bobby got sucked"