# Other
import webview
from random import choice
from string import ascii_uppercase
# Flask
from flask import render_template, url_for, redirect, jsonify, flash
# Local
from backend import app, db
from backend.models import Word, Preference
from backend.forms import WordForm, LivesForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/game')
def game():
    words = Word.query.all()
    if words:
        word = choice(words).word.upper()
    else:
        word = "HANGMAN"
    lives = 9
    letters = ascii_uppercase
    return render_template('game.html', letters=letters, word=word, lives=lives)


@app.route('/settings')
def settings():
    lives_form = LivesForm()
    words_form = WordForm()
    pref = Preference.query.get(1)
    lives = pref.lives
    words = Word.query.order_by(Word.id.desc()).all()
    return render_template('settings.html', lives=lives, lives_form=lives_form, words_form=words_form, words=words)


@app.route('/update-lives', methods=['POST'])
def update_lives():
    form = LivesForm()
    prefs = Preference.query.get(1)
    if form.validate_on_submit():
        prefs.lives = form.lives.data
        db.session.commit()

    lives_count = prefs.lives
    response = {
        'category': 'success',
        'message': f'Lives was updated to {lives_count}',
        'lives': lives_count
    }
    return jsonify(response)


@app.route('/restore-words')
def restore_words():
    # Reset the table
    db.session.query(Word).delete()
    db.session.commit()

    # Add the default words
    Word.init_default()
    words = Word.query.order_by(Word.id.desc()).all()

    template = render_template('partials/words_list.html', words=words)
    response = {'template': template}
    return jsonify(response)


@app.route('/add-word', methods=['POST'])
def add_word():
    form = WordForm()
    if form.validate_on_submit():
        word = Word(word=form.word.data)
        db.session.add(word)
        db.session.commit()

    words = Word.query.order_by(Word.id.desc()).all()
    template = render_template('partials/words_list.html', words=words)
    response = {'template': template}
    return jsonify(response)


@app.route('/remove-word/<int:pk>')
def remove_word(pk):
    word_to_delete = Word.query.get(pk)
    if word_to_delete:
        db.session.delete(word_to_delete)
        db.session.commit()

    words = Word.query.order_by(Word.id.desc()).all()
    template = render_template('partials/words_list.html', words=words)
    response = {'template': template}
    return jsonify(response)


@app.route('/delete-all-words', )
def delete_all_words():
    # Delete all words
    db.session.query(Word).delete()
    db.session.commit()

    words = Word.query.order_by(Word.id.desc()).all()
    template = render_template('partials/words_list.html', words=words)
    response = {'template': template}
    return jsonify(response)


@app.route('/quit')
def quit_app():
    window = webview.windows[0]
    result = window.create_confirmation_dialog(message="Quit", title="Are you sure you want to quit?")
    if not result:
        return redirect(url_for('home'))

    window.destroy()
    return render_template('quit.html')
