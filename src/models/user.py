
from database import db

class User(db.Model):
    __tablename__ = "users"

    id        = db.Column(db.Integer, primary_key=True)
    fbId      = db.Column(db.String(250), unique=True)
    email     = db.Column(db.String(250), unique=True)
    firstName = db.Column(db.String(250))
    lastName  = db.Column(db.String(250))
    name      = db.Column(db.String(250))
    gender    = db.Column(db.String(250))

    def __init__(self,
        fbId,
        email,
        firstName,
        lastName,
        name,
        gender):

        self.fbId      = fbId
        self.email     = email
        self.firstName = firstName
        self.lastName  = lastName
        self.name      = name
        self.gender    = gender

    def serialize(self):

        return {
            "id":    self.id,
            "fbId":  self.fbId,
            "email": self.email,
            "name":  self.name
        }
