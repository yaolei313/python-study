#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """student's name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name
