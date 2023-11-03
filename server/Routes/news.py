from flask import Blueprint, jsonify, Request
from Controllers.news import read_headlines_from_csv
from Controllers.news import get_rand_news
import Middleware.auth as mid

newsBP = Blueprint('news',__name__)

@newsBP.route('news', methods=['GET'])
def get_all_news():
    headlines = read_headlines_from_csv()
    return jsonify({'headlines': headlines})

# API endpoint to get 10 news headlines

@newsBP.route('randnews/<int:index>', methods=['GET'])
@mid.token_required
def rand_news_route(index):
    news=get_rand_news(index)
    return jsonify({'headlines':news})
    

# API endpoint to get a specific news headline by index
@newsBP.route('news/<int:index>', methods=['GET'])
def get_news_by_index(index):
    headlines = read_headlines_from_csv()
    if 0 <= index < len(headlines):
        return jsonify(headlines[index])
    else:
        return jsonify({'message': 'News not found'}), 404



