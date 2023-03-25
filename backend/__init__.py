# Flask
from flask import Flask, render_template, session, redirect
# Other modules
from pathlib import Path
import webview

# Flask App
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIRS = BASE_DIR / 'frontend/templates'
STATIC_DIRS = BASE_DIR / 'frontend/static'

app = Flask(__name__, static_folder=STATIC_DIRS, template_folder=TEMPLATE_DIRS)

# App Configs
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}/backend/hangman.db'
app.config['SECRET_KEY'] = 'SECRET-KEY-HERE'


# App Routes
@app.route('/')
def home():
    score = session.get('score', None)
    if not score:
        session['score'] = 10
    return render_template('home.html')


@app.route('/game/')
def game():
    return render_template('game.html')


@app.route('/settings/')
def settings():
    score = session.get('score')
    return render_template('settings.html', score=score)
