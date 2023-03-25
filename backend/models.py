# Other
import json
from pathlib import Path
# Local
from backend import db


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)

    @staticmethod
    def from_json(path: Path = None):
        CURRENT_DIR = Path(__file__).resolve().parent
        path = CURRENT_DIR / 'database/words.json'

        try:
            with open(path, 'r') as f:
                _data = json.load(f)
        except:
            print(f"Problem loading words from {path}")
            return

        _words = _data.get('words', None)
        if not _words:
            print(f"The provided json file doesnt contain any words, {path}")
            return

        instances = [Word(word=x) for x in _words]
        db.session.add_all(instances)
        db.session.commit()

    def __str__(self):
        return self.word


db.create_all()

words = Word.query.all()
if not words:
    Word.from_json()
