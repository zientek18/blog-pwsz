#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__,
            static_url_path='',
            static_folder='sources',
            template_folder='views')

app.config.update(
    DEBUG=True,
    SECRET_KEY='!qaz@wsX#EdC!@#AQ!^!ZEPQ!@*#ZNam&!(#Z'
)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from app import db
from app import routes