import csv
from flask import jsonify, Request
import random
csv_filename = 'data_scraper.csv'
def read_headlines_from_csv():
    headlines = []
    with open(csv_filename,  'r', encoding = 'cp850', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            headlines.append(row)
    return headlines
# API endpoint to get all news headlines

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