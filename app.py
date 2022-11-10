#Config

from flask import Flask

#instantiate flask

app= Flask(__name__)

#root route

@app.route("/")
def index():
    return "Hello, this is pet fax"

# pets index route
@app.route ('/pets')
def pets():
    return "These are our pets available for adoption!"

