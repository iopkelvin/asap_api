from db import db
from marshmallow import Schema, fields


class MemberSchema(Schema):



class MemberModel(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.Date)
    country = db.Column(db.String(2))

    # Parameters to be expected
    def __init__(self, first_name, last_name, dob, country):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.country = country

    # Json response
    def json(self):
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'dob': self.dob,
                'country': self.country
                }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
