# Other
import webview
# Flask
from flask import render_template, url_for, redirect, jsonify
# Local
from backend import app, db
from backend.models import Word
from backend.forms import WordForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/settings')
def settings():
    form = WordForm()
    words = Word.query.order_by(Word.id.desc()).all()
    return render_template('settings.html', form=form, words=words)


@app.route('/restore-words')
def restore_words():
    # Reset the table
    db.session.query(Word).delete()
    db.session.commit()

    # Add the default words
    Word.from_json()
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
    form = WordForm()
    word_to_delete = Word.query.get(pk)
    if word_to_delete:
        db.session.delete(word_to_delete)
        db.session.commit()

    words = Word.query.order_by(Word.id.desc()).all()
    return render_template('settings.html', form=form, words=words)


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
