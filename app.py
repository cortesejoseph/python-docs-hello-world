from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World, this is the first JoeC App service Web app"
