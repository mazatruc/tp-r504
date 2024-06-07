from flask import render_template, request, redirect, url_for
from app import app, db
from werkzeug.security import generate_password_hash
from app.forms import RegistrationForm
from app.models import User

@app.route('/')
def home():
    return render_template('templates/home.html')

@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data

        user_exists = User.query.filter_by(username=username).first()
        email_exists = User.query.filter_by(email=email).first()

        if user_exists or email_exists:
            message = 'Identifiant ou e-mail déjà utilisé.'
            return render_template('newuser.html', form=form, message=message)

        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

        message = 'Utilisateur créé avec succès !'
        return render_template('newuser.html', form=form, message=message)
    return render_template('newuser.html', form=form)

@app.route('/liste')
def liste():
    users = User.query.all()
    return render_template('liste.html', users=users)

@app.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            response = make_response(redirect(url_for('home')))
            response.set_cookie('username', username)
            return response

        message = 'Identifiant ou mot de passe incorrect.'
        return render_template('connect.html', message=message)

    return render_template('connect.html')
