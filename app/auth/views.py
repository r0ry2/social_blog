from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('main.index'))
        flash("Invalid email or password.")
    return render_template("auth/login.html", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please login.")
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html", form=form)
