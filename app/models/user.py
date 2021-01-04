from run import app, db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    type = db.Column(db.String(200))
    link = db.Column(db.String(200))
