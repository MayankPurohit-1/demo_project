from werkzeug.security import safe_str_cmp
from Database.connection import ConnectionModel


class SecurityModel:
    user_collection = ConnectionModel.connect('user_collection')

    @staticmethod
    def authenticate(username, password):
        temp = SecurityModel.user_collection.find_one({"username": username})
        print(temp)
        if temp and safe_str_cmp(temp['password'], password):
            return temp
        # usrname = request.form['username']
        # passwd = request.form['password']
        # data = request.get_json()
        # if usrname == temp['username'] and passwd == temp['password']:
        # if data['username'] == temp['username'] and data['password'] == temp['password']:
        #     return temp

    @staticmethod
    def identity(payload):
        temp_user = payload['identity']
        return SecurityModel.user_collection.find_one({"username": temp_user})
