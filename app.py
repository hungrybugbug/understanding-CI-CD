from flask import Flask

app = Flask(__name__)

@app.route("/login")
def login():
    return "Login Page"
@app.route("/")
def home():
    return "Hello, GitHub Act!"


