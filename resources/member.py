from flask import request, jsonify
from flask_restful import Resource
import json
import datetime
# from flask_jwt import jwt_required
from models.member import MemberModel

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


class MemberId(Resource):
    def post(self, member_id):
        json_data = request.get_json()


        member = MemberModel(member_id, **json_data)
        try:
            member.save_to_db()
        except ValueError:
            return {"message": "An error occurred inserting the item."}, 500  # Internal server error

        return json.dumps(member, default=myconverter), 201  # created status code


class MemberList(Resource):
    def get(self):
        # List comprehensions version
        return {'members': [member.json() for member in MemberModel.find_all()]}
