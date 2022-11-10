from flask import Flask, request

# factory function

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello PetFax!!"

    from . import pet
    app.register_blueprint(pet.bp)

    # # pets index route
    # @app.route ('/pets')
    # def pets_list():
    #     return "These are our new pets available for adoption!"

    # # contact route
    # @app.route ("/contact")
    # def contact():
    #     return "Here's our contact info!"

    # @app.route("/pets/<animal>", methods=["POST", "GET"])
    # def pets(animal=""):
    #     if request.method == "POST":
    #         return f"You chose a/an {animal}"
    #     else:
    #         return "List of Pets"

    return app