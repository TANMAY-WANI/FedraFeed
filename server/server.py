from flask import Flask, jsonify,request
import csv
from flask_cors import CORS, cross_origin
import random
# from scheduler import job
# from dataset_curator import scrape_and_save_headlines_to_csv

csv_filename = '../dataset/toi_headlines.csv'
app = Flask(__name__)
CORS(app, support_credentials=True, origins='*')


# Function to retrieve news headlines from the CSV file
def read_headlines_from_csv():
    headlines = []
    with open(csv_filename,  'r', encoding = 'cp850', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            headlines.append(row)
    return headlines




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

@app.route('/api/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    if request.method == 'POST' and 'Name' in request.form and 'Password' in request.form and 'Email' in request.form and 'Phone' in request.form:
        username = request.form['Name']
        password = request.form['Password']
        email = request.form['Email']
        phone = request.form['Phone']
        # use mongo db to store user details
        if user.find_one({"phone":phone}) is None:
            user.insert_one({"name":username,"email":email,"phone":phone,"password":password})
            return jsonify({'result': 'successfully signed up'})
        else:
            return jsonify({'result': 'successfully signed up'})
    else:
        return jsonify({'result': 'error'})

    


if __name__ == '__main__':
    # Start the scraping and writing task immediately
    # scheduled_scrape_and_write()

    # Start the Flask application
    # create_database()
    app.run(debug=True)