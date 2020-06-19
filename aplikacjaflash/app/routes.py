#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from flask import redirect, url_for, request, abort, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from app.services import UserService, PostService


# settings flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route("/")
@app.route('/index')
def main():
    return render_template('index.html')


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ids = request.form['id']

        PostService.update('', ids, title, description)

        return redirect(url_for("admin"))

    else:
        posts = PostService.getAll('')
        title = 'Admin'
        return render_template('admin.html', title=title, posts=posts)


@app.route("/removePost", methods=["POST"])
@login_required
def removePost():
    if request.method == 'POST':
        PostService.remove('', request.form['id'])

    return redirect(url_for("admin"))


@app.route("/addPost", methods=["POST"])
@login_required
def addPost():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        PostService.add('', title, description)

    return redirect(url_for("admin"))


@app.route("/info")
def info():
    title = "Blog"
    posts = PostService.getAll('')

    return render_template('news.html', title=title, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    title = 'Zaloguj się'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserService.get("", username, password)

        if user is not None:
            login_user(user)
            return redirect(url_for("admin"))

        else:
            return abort(401)

    else:
        return render_template('login.html', title=title)


@app.errorhandler(401)
def page_not_found(e):
    title = "Coś poszło nie tak..."
    error = "401"
    return render_template('error.html', title=title, error=error)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    title = "Wylogowanie"
    return render_template('logout.html', title=title)


# reload user
@login_manager.user_loader
def load_user(userid):
    return UserService.getById('', userid)
