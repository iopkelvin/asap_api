from flask import request, jsonify
from flask_restful import Resource
import json
# from flask_jwt import jwt_required
from models.member import MemberModel


class MemberId(Resource):
    def post(self, member_id):
        json_data = request.get_json()


        member = MemberModel(member_id, **json_data)
        try:
            member.save_to_db()
        except ValueError:
            return {"message": "An error occurred inserting the item."}, 500  # Internal server error

        return jsonify(member), 201  # created status code

