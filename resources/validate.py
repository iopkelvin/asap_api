from flask import request, render_template
from flask_restful import Resource

from models.member import MemberModel
from webargs import flaskparser, fields


FORM_ARGS = {
    'member_id': fields.Integer(required=True)}


class Validate(Resource):
    def post(self, member_id):
        member_id = request.form.get('member_id')

        if MemberModel.find_by_id(member_id):
            message = "Correct member id"
        else:
            message = "Wrong member id"


        return render_template('form.html', message=message)
