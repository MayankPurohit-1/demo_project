from Database.connection import ConnectionModel
from Model.UserModel import User
from bson import ObjectId


class SecurityModel:
    @staticmethod
    def authenticate(username, password):
        user = ConnectionModel.connect("user_collection").find_one({"username": username, "password": password})
        n = User(str(user['_id']), user['username'], user['password'])
        print(type(n))
        return n

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        result = ConnectionModel.connect("user_collection").find_one({"_id": ObjectId(user_id)})
        n = User(str(result['_id']), result['username'], result['password'])
        return n
