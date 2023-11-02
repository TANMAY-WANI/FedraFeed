from flask import Flask, jsonify,request
import requests
import csv
from flask_cors import CORS, cross_origin
import random
import mysql.connector as sqltor


app = Flask(__name__)
CORS(app, support_credentials=True, origins='*')
# Database configuration



# pref_data = {
#     'user_id':'1',
#     'category':'Politics'
# }
# user_data = {
#     'name':'Tanmay',
#     'email':'tanmay@gmail.com',
#     'phone':'9104332789',
#     'password':'1234'

# }
# news_data = {
#     'user_id':'1',
#     'news_headline':'Tanmay',
#     'img_url':'Hello world',
#     'news_body':'9104332789',
#     'news_url':'1234'
# }



# applying CORS to blueprints
import Routes.user
import Routes.news
CORS(Routes.user.userBP, support_credentials=True, origins='*')
CORS(Routes.news.newsBP, support_credentials=True, origins='*')

# Registering the blueprints for the routes
app.register_blueprint(Routes.user.userBP, url_prefix='/user')
app.register_blueprint(Routes.news.newsBP, url_prefix='/news')

def create_table():
    try :
        conn = sqltor.connect(host ="localhost",user="root",password="21BCP095",database="fedrafeed")
        if conn.is_connected():
            print("Successfully Connected !!")
        else:
            print("Failed to connect")
    except Exception as e:
        print("Error :",str(e))

# Function to retrieve news headlines from the CSV file



# @app.route('/signup',methods= ['POST'])
# @cross_origin(supports_credentials=True)
# def signup():
#     if request.method == 'POST' and 'Name' in request.form and 'Password' in request.form and 'Email' in request.form and 'Phone' in request.form:
#         username = request.form['Name']
#         password = request.form['Password']
#         email = request.form['Email']
#         phone = request.form['Phone']
#         if check_user(phone):
#             return jsonify({'result': 'user already exists'})
#         else:
#             usr_info = [username,email,phone,password]
#             insert_data(usr_info)
#             return jsonify({'result': 'successfully signed up'})
#     else:
#         return jsonify({'result': 'error'})



@app.route('/api/payments',methods = ['POST'])
@cross_origin(supports_credentials=True)
def payments():
    # order_id = request.form['customerId']+str(time.time())
    order_id = request.form['customerId']+str(random.randint(0,100000))
    print(order_id)
    data = {
        "order_id":order_id,
        "order_amount": request.form['amount'],
      "order_currency": 'INR',
      "order_note": request.form['plan'],
      "customer_details": {
        "customer_id": request.form['customerId'],
        "customer_phone": '9816512345',
      },
      "order_meta":{"return_url":f'http://localhost:3000/payment/success?order_id={order_id}'}
    }
    
    headers = {
      'Content-Type': 'application/json',
      'x-api-version': '2022-09-01',
      'x-client-id': 'TEST3621937e388945e171510d9db0391263',
      'x-client-secret': 'TEST9a1fe026bbe5f76a889a4ed5e181b8b8775d72c',
    }
    #post request to create order
    response = requests.post('https://sandbox.cashfree.com/pg/orders', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else :
        return response.json()
if __name__ == '__main__':
    # create_tables()
    app.run(debug=True)