from flask_jwt import jwt_required
from flask_restful import Resource
from flask import render_template, request, make_response
from Model.UserModel import User


class user_register(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template('register.html'), headers)

    def post(self):
        t = User()
        name_temp = request.form['name']
        user_name = request.form['username']
        password_temp = request.form['password']
        headers = {"Content-Type": "text/html"}
        return make_response(t.userRegistration(name_temp, user_name, password_temp), headers)


class login(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template('login.html', title="Login Here!"), headers)

    @jwt_required
    def post(self):
        t = User()
        data = request.get_json()
        headers = {"Content-Type": "text/html"}
        return make_response("Login successful", data , headers)




