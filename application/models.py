from application import db
from flask_login import UserMixin
from datetime import datetime



class Posts(db.Model):#User-Vocab
    id = db.Column(db.Integer, primary_key=True) 
    englishh = db.Column(db.String(100), nullable=False, unique=True) #
    spanishh = db.Column(db.String(100), nullable=False, unique=True)
    comment = db.Column(db.String(100), nullable=True, unique=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return ''.join([
            'User ID: ', self.user_id, '\r\n',
            'Title: ', self.title, '\r\n', self.content
        ])

#Users-Vocab = db.Table('User-Vocab',
#   db.Column('userID', db.Integer, db.ForeignKey('Users.userID')),
#   db.Column('vocabID', db.Integer, db.ForeignKey('vocabID')),
#   comment = db.Column(db.String(100), nullable=True, unique=False),
#   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#   )

#class Users-Vocab(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    userID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#    vocabID = db.Column(db.Integer, db.ForeignKey('vocabulary.id'), nullable=False)
#    comment = db.Column(db.String(100), nullable=True, unique=False)
#    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #userID = 
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n', 
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

#class Vocabulary(db.Model):
#    vocabID = db.Column(db.Integer, primary_key=True)
#    englishh = db.Column(db.String(100), nullable=False, unique=True)
#    spanishh = db.Column(db.String(100), nullable=False, unique=True)

 #   def __repr__(self):
  #      return ''.join([
   #         'User ID: ', self.user_id, '\r\n',
    #        'Title: ', self.title, '\r\n', self.content
     #   ])

