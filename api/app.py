from flask import Flask
from flask_cors import CORS
from models import Subject

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
breakpoint()

import routes