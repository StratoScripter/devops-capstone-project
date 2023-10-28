from flask_talisman import Talisman
from flask import Flask


# After the Flask app is created
app = Flask(__name__)

# Create an instance of the Talisman class
talisman = Talisman(app)
