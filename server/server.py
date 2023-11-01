from flask import Flask, jsonify,request
import requests
import csv
from flask_cors import CORS, cross_origin
import random
import os
import time
import mysql.connector as sqltor

try :
    conn = sqltor.connect(host ="localhost",user="root",password="66121200",database="fedrafeed")
    if conn.is_connected():
        print("Successfully Connected !!")
        cur=conn.cursor()
    else:
        print("Failed to connect")
except Exception as e:
    print("Error :",str(e))

def create_tables():
    cmd1 = '''create table users(
        user_id int not null auto_increment primary key,
        name varchar(20),
        email varchar(50) not null,
        phone varchar(10) not null,
        password varchar(20) not null)'''
    
    cmd2 = '''create table saved_news(
    user_id int not null,
    news_headline varchar(100) not null,
    img_url varchar(100) not null,
    news_body varchar(300) not null,
    news_url varchar(100) not null,
    foreign key (user_id) references users(user_id)
    )'''

    cmd3 = '''create table user_preferences(
    user_id int not null,
    Politics int not null default 0,
    Sports int not null default 0,
    Technology int not null default 0,
    Entertainment int not null default 0,
    National int not null default 0,
    foreign key (user_id) references users(user_id)
    )'''
    cur.execute(cmd1)
    cur.execute(cmd2)
    cur.execute(cmd3)
    conn.commit()
    print("table created")

def  insertUser(user_data):
    try:
        name = user_data['name']
        email = user_data['email']
        phone = user_data['phone']
        password = user_data['password']
        cmd1 = "insert into users(name,email,phone,password) values(%s, %s, %s, %s)"
        cmd2 = 'select user_id from users where phone = %s'
        cmd3 = 'insert into user_preferences (user_id) values(%s)'

        data = (name,email,phone,password)
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


pref_data = {
    'user_id':'1',
    'category':'Politics'
}
# create_tables()
user_data = {
    'name':'Tanmay',
    'email':'tanmay@gmail.com',
    'phone':'9104332789',
    'password':'1234'

}

news_data = {
    'user_id':'1',
    'news_headline':'Tanmay',
    'img_url':'Hello world',
    'news_body':'9104332789',
    'news_url':'1234'
}


app = Flask(__name__)
CORS(app, support_credentials=True, origins='*')


csv_filename = 'data_scraper.csv'

def create_table():
    try :
        conn = sqltor.connect(host ="localhost",user="root",password="21BCP095",database="fedrafeed")
        if conn.is_connected():
            print("Successfully Connected !!")
        else:
            print("Failed to connect")
    except Exception as e:
        print("Error :",str(e))
    
# import sqlite3
# con = sqlite3.connect("fedra_feed.db")
# cur = con.cursor()

# def create_database():
#     cur.execute("""CREATE TABLE USERS(
#             NAME VARCHAR,
#             EMAIL VARCHAR NOT NULL,
#             PHONE VARCHAR NOT NULL PRIMARY KEY,
#             PASSWORD VARCHAR NOT NULL)""")

# def insert_data(usr_info):
#     cur.execute("INSERT INTO USERS VALUES(?,?,?,?)",usr_info)

# def check_user(phone):
#     cur.execute("SELECT PHONE FROM USERS WHERE PHONE = ?",(phone))
#     if cur.fetchone() is None:
#         return False
#     else:
#         return True
    

# Function to retrieve news headlines from the CSV file
def read_headlines_from_csv():
    headlines = []
    with open(csv_filename,  'r', encoding = 'cp850', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            headlines.append(row)
    return headlines


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


# API endpoint to get all news headlines
@app.route('/api/news', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_all_news():
    headlines = read_headlines_from_csv()
    return jsonify({'headlines': headlines})

# API endpoint to get 10 news headlines
@app.route('/api/randnews/<int:index>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_rand_news(index):
    headlines = read_headlines_from_csv()
    randomHeadlines=[]
    randomNumbers=[]
    while len(randomNumbers)<index:
        randomNum = random.randint(0, len(headlines)-1)
        if randomNum not in randomNumbers:
            randomNumbers.append(randomNum)
            randomHeadlines.append(headlines[randomNum])
    
    return jsonify({'headlines': randomHeadlines})

# API endpoint to get a specific news headline by index
@app.route('/api/news/<int:index>', methods=['GET'])
def get_news_by_index(index):
    headlines = read_headlines_from_csv()
    if 0 <= index < len(headlines):
        return jsonify(headlines[index])
    else:
        return jsonify({'message': 'News not found'}), 404

# @app.route('/api/chatroom',methods = ['POST'])
# def chatroom():
#     responce = requests.get('https://api.chatengine.io/users/me',
#                             headers={
#                                 "Project-ID":os.environ['CHAT_ENGINE_PROJECT_ID'],
#                                 "User-Name":"Tanmay",
                                
#                             })


@app.route('/addUser',methods = ['POST'])
@cross_origin(supports_credentials=True)
def signup():
    data = request.get_json()
    userid=insertUser(data)

    return jsonify({'result': 'successfully signed up'})


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