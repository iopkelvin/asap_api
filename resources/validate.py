from flask import request, render_template
from flask_restful import Resource

from models.member import MemberModel
from webargs import flaskparser, fields


FORM_ARGS = {
    'member_id': fields.Integer(required=True)}


class MemberId(Resource):
    def post(self, member_id):


        json_data = request.get_json()

        member = MemberModel(member_id, **json_data)
        try:
            member.save_to_db()
        except ValueError:
            return {"message": "An error occurred inserting the item."}, 500  # Internal server error

        return render_template('form.html')
