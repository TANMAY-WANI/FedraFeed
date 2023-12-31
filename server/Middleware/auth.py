from functools import wraps
from flask import request, jsonify
import jwt
import os
from Controllers.user import get_user_from_phone
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        print(token)
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, str(os.getenv('SECRET_KEY')), algorithms=['HS256'] )
            current_user = get_user_from_phone(data['id'])
        except Exception as e:
            print(e)
            return jsonify({
                'message' : "error"
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated
  