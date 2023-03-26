# Other
import webview
from random import choice
from string import ascii_uppercase
# Flask
from flask import render_template, url_for, redirect, jsonify
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
        word = choice(words).text
    else:
        word = "HANGMAN"

    pref = Preference.query.get(1)
    lives = pref.lives
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
    response = dict()
    form = LivesForm()
    prefs = Preference.query.get(1)

    if form.validate_on_submit():
        new_lives_count = form.lives.data
        prefs.lives = new_lives_count
        db.session.commit()
        response['message'] = f'Lives count was updated to {prefs.lives}'

    response['lives'] = prefs.lives
    return jsonify(response)


@app.route('/restore-words')
def restore_words():
    response = dict()

    # Reset the table
    db.session.query(Word).delete()
    db.session.commit()

    # Add the default words
    Word.init_default()
    words = Word.query.order_by(Word.id.desc()).all()
    response['message'] = f'Default words were restored successfully'

    template = render_template('partials/words_list.html', words=words)
    response['template'] = template
    return jsonify(response)


@app.route('/a1dd-word', methods=['POST'])
def add_word():
    response = dict()
    form = WordForm()

    if form.validate_on_submit():
        word_text = form.word.data.upper()
        already_exists = Word.query.filter_by(text=word_text).all()
        if already_exists:
            response['message'] = f'{word_text} Already exists in the words list'
        else:
            word = Word(text=word_text)
            db.session.add(word)
            db.session.commit()
            response['message'] = f'{word} was added successfully'

    words = Word.query.order_by(Word.id.desc()).all()
    template = render_template('partials/words_list.html', words=words)
    response['template'] = template

    return jsonify(response)


@app.route('/remove-word/<int:pk>')
def remove_word(pk):
    response = dict()
    word_to_delete = Word.query.get(pk)

    if word_to_delete:
        db.session.delete(word_to_delete)
        db.session.commit()
        response['message'] = f'{word_to_delete} was deleted successfully'

    words = Word.query.order_by(Word.id.desc()).all()
    template = render_template('partials/words_list.html', words=words)
    response['template'] = template
    return jsonify(response)


@app.route('/delete-all-words')
def delete_all_words():
    response = dict()

    # Delete all words
    db.session.query(Word).delete()
    db.session.commit()
    response['message'] = f'All words were deleted successfully'

    words = Word.query.order_by(Word.id.desc()).all()
    template = render_template('partials/words_list.html', words=words)
    response['template'] = template
    return jsonify(response)


@app.route('/quit')
def quit_app():
    window = webview.windows[0]
    result = window.create_confirmation_dialog(message="Quit", title="Are you sure you want to quit?")
    if not result:
        return redirect(url_for('home'))

    window.destroy()
    return render_template('quit.html')
