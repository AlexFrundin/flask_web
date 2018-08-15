from app import app, db
from flask import render_template, flash, redirect, url_for,request
from .forms import LoginForm, RegistrationForm, PetForm
from .models import User, Pet, Types, Info
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

@app.route('/add_pets',methods=['get','post'])
@login_required
def add_pets():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        type = Types.query.filter_by(type=form.type.data).first()
        pet = Pet(name=name, typepet=type, owner=current_user)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('pets'))
    return render_template('add_pets.html', form=form)
@app.route('/')
def root():
    if current_user.is_authenticated:
        flash("Добро пожаловать {}".format(current_user.login))
    else:
        flash("Для всех возможностей войдите в систему!")
    return render_template('index.html')

@app.route('/pets')
@login_required
def pets():
    # pets = Pet.query.filter(Pet.user_id.like(current_user.get_id()))
    pets = current_user.pets
    pets = pets.paginate(per_page=6)
    return render_template('pets.html',pets=pets, title="Welcome!")

@app.route('/registration', methods=['get','post'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        u = User(login,password)
        db.session.add(u)
        db.session.commit()
        login_user(user=u)
        return redirect(url_for('root'))
    return render_template('registration.html',form=form)

@app.route('/login', methods=['get', 'post'])
def login():
    if  current_user.is_authenticated:
        return redirect(url_for('pets'))
    form = LoginForm()
    if form.validate_on_submit():
        login = form.name.data
        password = form.password.data
        u = User.query.filter_by(login=login).first()
        if u is not None and u.check_password(password):
            login_user(user=u)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('pets')
            return redirect(next_page)
        else:
            flash("Не верные данные!")
    return render_template('login.html',title="Login", form=form)

@app.route('/logout')
def logout():
    flash("GoodBye")
    logout_user()
    return redirect(url_for('login'))



# @app.route('/test', methods=['get', 'post'])
# @login_required
# def test():
#     name = request.form.get('login_user')
#     password = request.form.get('pasw')
#     data = {name,password}
#     date_ = request.form.get('date')
#     print(date_)
#     return render_template("test.html",title="test", post_object=data)
#
@app.route('/user/<int:key>')

def user_name(key):
    return render_template('user_name.html',name=info[key])
