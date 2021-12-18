from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import os
import re
from datetime import datetime, timedelta
from functools import wraps
from pontotel.db import get_db
from .utils import dict_factory

bp = Blueprint('api', __name__)


# decorator for check JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, os.environ.get('SECRET_KEY'))
            user = get_db().execute(
                'SELECT * FROM user WHERE email = ?', (data['email'],)
            ).fetchone()
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(user, *args, **kwargs)

    return decorated


# login user
@bp.route('/login', methods=['POST'])
def api_login():
    auth = request.json
    email = auth['email']
    password = auth['password']
    response = 'Error: Try verify your username and password'

    if not auth or not email or not password:
        return make_response(jsonify({'message': response}), 401)

    user = get_db().execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()

    if not user:
        return make_response(jsonify({'message': response}), 401)

    if check_password_hash(user['password'], password):
        token = jwt.encode({
            'email': user['email'],
            'exp': datetime.utcnow() + timedelta(minutes=60)
        }, os.environ.get('SECRET_KEY'))

        return make_response(jsonify({'token': token.decode('UTF-8')}), 201)

    return make_response(jsonify({'message': response}), 401)


# register new user
@bp.route('/register', methods=['POST'])
def api_register():
    data = request.json
    email = data['email']
    password = data['password']
    name = data['name']
    country = data['country']
    federal_state = data['federal_state']
    city = data['city']
    cep = data['cep']
    street = data['street']
    residential_number = data['residential_number']
    aditional_address_info = data['aditional_address_info']
    cpf = data['cpf']
    pis = data['pis']

    db = get_db()
    error = None
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (
        not email or not password or not name or not country or
        not federal_state or not city or not cep or not street or
        not residential_number or not cpf or not pis
    ):
        error = 'Some required field is missing. Please verify'
        return make_response(jsonify({'message': error}), 422)
    elif not re.fullmatch(email_regex, email):
        error = 'Invalid email.'
        return make_response(jsonify({'message': error}), 422)

    if error is None:
        try:
            db.execute(
                "INSERT INTO user (email, password, name, country, federal_state, city, cep, street, residential_number, aditional_address_info, cpf, pis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (email, generate_password_hash(password), name, country, federal_state,
                 city, cep, street, residential_number, aditional_address_info, cpf, pis)
            )
            db.commit()

            return make_response('User registered.', 201)

        except db.IntegrityError:
            error = f"User {email} already exists."

            return make_response(jsonify({'message': error}), 409)


#  get logged user data
@bp.route('/profile', methods=['GET'])
@token_required
def api_get_user(user):
    db = get_db()
    
    db.row_factory = dict_factory
    cursor = db.cursor()
    user_data = cursor.execute(
        'SELECT * FROM user WHERE email = ?', (user['email'],)
    ).fetchone()

    print(user_data)

    return jsonify(user_data)


# update logged user data
@bp.route('/profile', methods=['POST'])
@token_required
def api_update_user(user):
    data = request.json
    name = data['name']
    country = data['country']
    federal_state = data['federal_state']
    city = data['city']
    cep = data['cep']
    street = data['street']
    residential_number = data['residential_number']
    aditional_address_info = data['aditional_address_info']
    cpf = data['cpf']
    pis = data['pis']

    error = None

    if (
        not name or not country or not federal_state or not city or
        not cep or not street or not residential_number or not cpf or
        not pis
    ):
        error = 'Some required field is missing. Please verify'
        return make_response(jsonify({'message': error}), 422)

    if error is None:
        db = get_db()
        db.execute(
            'UPDATE user SET name = ?, country = ?, federal_state = ?, city = ?, cep = ?, street = ?, residential_number = ?, aditional_address_info = ?, cep = ?, pis = ?'
            'where email = ?',
            (name, country, federal_state, city, cep, street,
                residential_number, aditional_address_info, cpf, pis, user['email'])
        ).fetchone()
        db.commit()

        return make_response(jsonify({'message': 'User updated.'}), 200)


# delete logged user
@bp.route('/profile', methods=['DELETE'])
@token_required
def api_delete_user(user):
    db = get_db()
    db.execute('DELETE FROM user WHERE email = ?', (user['email'],))
    db.commit()

    return make_response(jsonify({'message': 'User deleted.'}), 200)

