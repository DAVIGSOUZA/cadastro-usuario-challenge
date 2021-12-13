import functools
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from pontotel.db import get_db

bp = Blueprint('auth', __name__)


# register view
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        country = request.form['country']
        federal_state = request.form['federal_state']
        city = request.form['city']
        cep = request.form['cep']
        street = request.form['street']
        residential_number = request.form['residential_number']
        aditional_address_info = request.form['aditional_address_info']
        cpf = request.form['cpf']
        pis = request.form['pis']
        
        db = get_db()
        error = None

        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if  (
                not email or not password or not name or not country or 
                not federal_state or not city or not cep or not street or
                not residential_number or not cpf or not pis
            ):
            error = 'Preencha os campos requeridos.(*)'
        elif not re.fullmatch(email_regex, email):
            error = 'Informe um email válido.'
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (email, password, name, country, federal_state, city, cep, street, residential_number, aditional_address_info, cpf, pis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (email, generate_password_hash(password), name, country, federal_state, city, cep, street, residential_number, aditional_address_info, cpf, pis)
                )
                db.commit()
            except db.IntegrityError:
                error = f"Usuário {email} já existe."
            else:
                return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template('register.html')


# login view
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = "Usuário e/ou senha incorreto."
        elif not check_password_hash(user['password'], password):
            error = "Usuário e/ou senha incorreto."
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)
    
    return render_template('login.html')


@bp.before_app_request
def logged_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view
