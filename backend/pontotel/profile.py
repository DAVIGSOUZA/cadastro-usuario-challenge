from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from pontotel.auth import login_required
from pontotel.db import get_db

bp = Blueprint('profile', __name__)


def get_user(id):
    user = get_db().execute(
        'SELECT * FROM user where id = ?', (id,)
    ).fetchone()

    if user is None:
        abort(404, 'Usuário não existe.')
    
    if user['id'] != g.user['id']:
        abort(403)
    
    return user


@bp.route('/')
@login_required
def index():
    user_id = session.get('user_id')
    user = get_user(user_id)

    return render_template('index.html', user=user)


@bp.route('/update', methods=('GET', 'POST'))
@login_required
def update():
    user_id = session.get('user_id')
    user = get_user(user_id)
   
    if request.method == 'POST':
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

        error = None

        if  (
                not name or not country or not federal_state or not city or 
                not cep or not street or not residential_number or not cpf or 
                not pis
            ):
            error = 'Preencha os campos requeridos.(*)'
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE user SET name = ?, country = ?, federal_state = ?, city = ?, cep = ?, street = ?, residential_number = ?, aditional_address_info = ?, cep = ?, pis = ?'
                'where id = ?',
                (name, country, federal_state, city, cep, street, residential_number, aditional_address_info, cpf, pis, user_id)
            ).fetchone()
            db.commit()
            return redirect(url_for('profile.index'))
    
    return render_template('update.html', user=user)


@bp.route('/delete', methods=('POST',))
@login_required
def delete():
    user_id = session.get('user_id')
    db = get_db()
    db.execute('DELETE FROM user WHERE id = ?', (user_id,))
    db.commit()
    session.clear()
    return redirect(url_for('auth.login'))