from flask import request, jsonify
from flask_restful import Resource
# from flask_jwt import jwt_required
from models.member import MemberModel, MemberSchema
from marshmallow import ValidationError


class MemberId(Resource):
    def post(self, member_id):
        json_data = request.get_json()

        try:  # Make sure that input in equal to schema
            data = MemberSchema().load(json_data)
        except ValidationError as err:
            response = jsonify(err.messages)
            response.status_code = 422
            return response

        member = MemberModel(member_id, **data)
        try:
            member.save_to_db()
        except ValueError:
            return {"message": "An error occurred inserting the item."}, 500  # Internal server error

        return member.json(), 201  # created status code

