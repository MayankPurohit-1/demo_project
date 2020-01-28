from Database.connection import ConnectionModel


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        self.user_collection = ConnectionModel.connect('user_collection')

    def userRegistration(self, name, username, password):
        result = self.user_collection.count({'username': username})
        if result:
            return "User already exist"
        result = self.user_collection.insert_one({"name": name, "username": username, "password": password})
        if result.inserted_id:
            return "<p>User Added Successfully!</p>"

