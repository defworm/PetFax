# #Config

# from flask import Flask

# #instantiate flask (applications are initiated as an instance of Flaske. This can be done globally in a root app.py file.)

# app= Flask(__name__)

# #root route

# @app.route("/")
# def index():
#     return "Hello, this is pet fax"

# # pets index route
# @app.route ('/pets')
# def pets():
#     return "These are our pets available for adoption!"

from petfax import create_app

app = create_app()

