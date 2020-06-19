#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Post():
    __id = 0
    __name = ""
    __text = ""

    def __init__(self, id, title, text):
        self.id = id
        self.__title = title
        self.__text = text

    def id(self):
        return self.__id

    def title(self):
        return self.__title

    def text(self):
        return self.__text
