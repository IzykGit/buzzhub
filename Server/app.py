from flask import Flask, Blueprint
from flask_cors import CORS
from flask_talisman import Talisman


def create_app():
    
    app = Flask(__name__)
    CORS(app)
    Talisman(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)