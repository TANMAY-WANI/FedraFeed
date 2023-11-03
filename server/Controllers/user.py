from datetime import datetime, timedelta
import mysql.connector as sqltor
from flask import request, jsonify, make_response
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
conn  = sqltor.connect(host="localhost", user="root", password="66121200", database="FEDRAFEED")
cur = conn.cursor()
def  insertUser(user_data):
    try:
        name = user_data['name']
        email = user_data['email']
        phone = user_data['phone']
        password = user_data['password']
        hashed=generate_password_hash(password)
        cmd1 = "insert into users(name,email,phone,password) values(%s, %s, %s, %s)"
        cmd2 = 'select user_id from users where phone = %s'
        cmd3 = 'insert into user_preferences (user_id) values(%s)'

        data = (name,email,phone,hashed)
        cur.execute(cmd1,data)
        cur.execute(cmd2,(phone,))
        output = cur.fetchone()

        cur.execute(cmd3,(output[0],))
        conn.commit()
        return output[0]
    except Exception as e:
        print("Error :",str(e))

def insert_saved_news(news_data):
    try:
        user_id = news_data['user_id']
        news_headline = news_data['news_headline']
        img_url = news_data['img_url']
        news_body = news_data['news_body']
        news_url = news_data['news_url']
        cmd = "insert into saved_news(user_id,news_headline,img_url,news_body,news_url) values(%s, %s, %s, %s, %s)"
        data = (user_id,news_headline,img_url,news_body,news_url)
        cur.execute(cmd,data)
        conn.commit()
        print("Data inserted")

    except Exception as e:
        print("Error :",str(e))

def insert_user_preferences(user_preferences_data):
    try:
        user_id = user_preferences_data['user_id']
        category = user_preferences_data['category']
        cmd = f"UPDATE user_preferences SET {category} = {category} + 1 WHERE user_id = %s"
        cur.execute(cmd,(user_id,))
        conn.commit()
        print("Data inserted")
    except Exception as e:
        print("Error :",str(e))

# def get_user_from_id():
def get_user_from_email():
    print("Inside get_user_from_email")

def get_user_from_phone(phone):
    cmd = "SELECT password FROM users WHERE phone = %s"
    cur.execute(cmd, (phone,))
    user = cur.fetchone()
    if user == None:
        print("User not found")
        return None
    print("Fetched user successfully")
    return user[0]

def login(phone,password):
    # creates dictionary of form data
  
    if not phone or not password:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = get_user_from_phone(phone)
    print(user)
    print(password)
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user, password):
        # generates the JWT Token
        token = jwt.encode({
            'id': str(phone),
            'exp' : datetime.utcnow() + timedelta(minutes = 60)
        }, str(os.getenv('SECRET_KEY')))
  
        return make_response(jsonify({'token' : token}), 201)
    # returns 403 if password is wrong
    else: return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )