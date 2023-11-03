import json
from flask import Blueprint, jsonify, request
from Controllers.user import insertUser , insert_saved_news , insert_user_preferences, login

userBP = Blueprint('user',__name__)

@userBP.route('/addUser',methods = ['POST'])
def addUser():
    data = request.get_json()
    userid=insertUser(data)
    return jsonify({'result': 'successfully signed up'}), 200

@userBP.route('/addSavedNews',methods = ['POST'])
def addSavedNews():
    data = request.get_json()
    insert_saved_news(data)
    return jsonify({'result': 'successfully inserted'}), 200

@userBP.route('/addUserPreferences',methods = ['POST'])
def addUserPreferences():
    data = request.get_json()
    insert_user_preferences(data)
    return jsonify({'result': 'successfully inserted'}), 200

@userBP.route('/login',methods = ['POST'])
def loginRoute():
    data = request.get_json()
    res=login(data['phone'],data['password'])
    return res


