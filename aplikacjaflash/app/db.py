#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
from app import app
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title

"""
db.create_all();

p = hashlib.sha512("Python123").encode('utf-8').hexdigest()
print(p)

#admin = User(username='kziniewicz', email='kamil@ziniewicz.pl', password=p)
#db.session.add(admin)
#db.session.commit()

admin = User(username='kziniewicz', email='kamil@ziniewicz.pl', password='Python123')
db.session.add(admin)
db.session.commit()

"""