# Other modules
import webview
from pathlib import Path
# Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Flask App
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIRS = BASE_DIR / 'frontend/templates'
STATIC_DIRS = BASE_DIR / 'frontend/static'

app = Flask(__name__, static_folder=STATIC_DIRS, template_folder=TEMPLATE_DIRS)
app.app_context().push()

# App Configs
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}/backend/database/hangman.db'
app.config['SECRET_KEY'] = 'SECRET-KEY-HERE'

# Database manager
db = SQLAlchemy(app)

# App models
from backend import models

# App Routes
from backend import views
