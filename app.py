from flask_restful import Api
from flask import Flask
from Routes.routes import user_register
from Routes.routes import login
from Routes.routes import example
from Model.SecurityModel import SecurityModel
from flask_jwt import JWT

app = Flask(__name__)
app.secret_key = 'masterkey'
api = Api(app)


jwt = JWT(app, SecurityModel.authenticate, SecurityModel.identity)

api.add_resource(user_register, '/register')
api.add_resource(login, '/login')
api.add_resource(example, '/example')
app.run(debug=True)
