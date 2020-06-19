#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.db import db, User, Post


class UserService:
    def __init__(self):
        pass

    def get(self, email, password):
        user = db.session.query(User).filter(User.password == password and User.email == email).first()

        return user

    def getById(self, userid):
        user = db.session.query(User).filter(User.id == userid).first()

        return user


class PostService:
    def __init__(self):
        pass

    def getAll(self):
        return db.session.query(Post).all()

    def add(self, title, description):
        post = Post(title=title, body=description)
        db.session.add(post)
        db.session.commit()

    def remove(self, id):
        post = db.session.query(Post).filter(Post.id == id).first();
        db.session.delete(post)
        db.session.commit()

    def update(self, id, title, description):
        post = db.session.query(Post).filter(Post.id == id).first()
        post.body = description
        post.title = title
        db.session.commit()