from flask import Flask, jsonify,request
import csv
from flask_cors import CORS, cross_origin
import random
# from scheduler import job
# from dataset_curator import scrape_and_save_headlines_to_csv

app = Flask(__name__)
CORS(app, support_credentials=True, origins='*')


csv_filename = '../dataset/toi_headlines.csv'

import sqlite3
con = sqlite3.connect("fedra_feed.db")
cur = con.cursor()

def create_database():
    cur.execute("""CREATE TABLE USERS(
            NAME VARCHAR,
            EMAIL VARCHAR NOT NULL,
            PHONE VARCHAR NOT NULL PRIMARY KEY,
            PASSWORD VARCHAR NOT NULL)""")

def insert_data(usr_info):
    cur.execute("INSERT INTO USERS VALUES(?,?,?,?)",usr_info)

def check_user(phone):
    cur.execute("SELECT PHONE FROM USERS WHERE PHONE = ?",(phone))
    if cur.fetchone() is None:
        return False
    else:
        return True
    

# Function to retrieve news headlines from the CSV file
def read_headlines_from_csv():
    headlines = []
    with open(csv_filename,  'r', encoding = 'cp850', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            headlines.append(row)
    return headlines


@app.route('/signup',methods= ['POST'])
@cross_origin(supports_credentials=True)
def signup():
    if request.method == 'POST' and 'Name' in request.form and 'Password' in request.form and 'Email' in request.form and 'Phone' in request.form:
        username = request.form['Name']
        password = request.form['Password']
        email = request.form['Email']
        phone = request.form['Phone']
        if check_user(phone):
            return jsonify({'result': 'user already exists'})
        else:
            usr_info = [username,email,phone,password]
            insert_data(usr_info)
            return jsonify({'result': 'successfully signed up'})
    else:
        return jsonify({'result': 'error'})


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


    


if __name__ == '__main__':
    # Start the scraping and writing task immediately
    # scheduled_scrape_and_write()

    # Start the Flask application
    # create_database()
    app.run(debug=True)