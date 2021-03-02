from db import db
from marshmallow import Schema, fields


class MemberSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    dob = fields.Date(required=True)
    country = fields.String(required=True)


class MemberModel(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.Date)
    country = db.Column(db.String(2))

    # Parameters to be expected
    def __init__(self, member_id, first_name, last_name, dob, country):
        self.member_id = member_id
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
