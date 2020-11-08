from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models import Subject

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

import routes