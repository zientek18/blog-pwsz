#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Page():
    __title = ""
    __text = ""

    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    def title(self):
        return self.__title

    def text(self):
        return self.__text
