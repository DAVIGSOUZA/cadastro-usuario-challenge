from flask import json, request, jsonify, Blueprint, make_response
from werkzeug.security import check_password_hash
import jwt
import os
from datetime import datetime, timedelta
from functools import wraps
from pontotel.db import get_db

bp = Blueprint('api', __name__)


# decorator for check JWT
def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None
    
    if 'x-access-token' in request.headers:
      token = request.headers['x-access-token']
    
    if not token:
      return jsonify({'message' : 'Token is missing'}), 401

    try:
      data = jwt.decode(token, os.environ.get('SECRET_KEY'))
      user = get_db().execute(
        'SELECT * FROM user WHERE email = ?', (data['email'],)
      ).fetchone()
    except:
      return jsonify({'message' : 'Token is invalid'}), 401
    
    return f(user, *args, **kwargs)

  return decorated


# route for login user
@bp.route('/login', methods=['POST'])
def login():
  auth = request.json
  email = auth['email']
  password = auth['password']
  response = 'Error: Try verify your username and password'

  if not auth or not email or not password:
    return make_response(response, 401)
  
  user = get_db().execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()

  if not user:
    return make_response(response, 401)
  
  if check_password_hash(user['password'], password):
    token = jwt.encode({
      'email': user['email'],
      'exp': datetime.utcnow() + timedelta(minutes = 60)
    }, os.environ.get('SECRET_KEY'))

    return make_response(jsonify({'token': token.decode('UTF-8')}), 201)

  return make_response(response, 401)




# api_register_user

# api_get_user

# api_update_user

# api_delete_user