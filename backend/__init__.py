# Other modules
import os
from pathlib import Path
# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask App
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIRS = BASE_DIR / 'frontend/templates'
STATIC_DIRS = BASE_DIR / 'frontend/static'
DATABASE_DIR = BASE_DIR / 'database'

app = Flask(__name__, static_folder=STATIC_DIRS, template_folder=TEMPLATE_DIRS)
app.app_context().push()

# App Configs
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_DIR}/hangman.db"
app.config['SECRET_KEY'] = 'SECRET-KEY-HERE'

# Database manager
db = SQLAlchemy(app)
if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

# App models
from backend import models

# App Routes
from backend import views
