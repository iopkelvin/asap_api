from flask import request, render_template
from flask_restful import Resource
# from flask_jwt import jwt_required
from models.member import MemberModel
from marshmallow import ValidationError
from wtforms import Form, TextField, TextAreaField, validators, StringField

# class ReusableForm(Form):
#     member_id = TextField('member_id:' validators=[validators.required()])


class MemberId(Resource):
    def post(self, member_id):
        # form = ReusableForm(request.form)

        json_data = request.get_json()

        member = MemberModel(member_id, **json_data)
        try:
            member.save_to_db()
        except ValueError:
            return {"message": "An error occurred inserting the item."}, 500  # Internal server error

        return render_template('form.html')
