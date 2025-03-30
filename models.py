from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BorrowedWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(200), nullable=False)
    definition = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<BorrowedWord {self.word}>'