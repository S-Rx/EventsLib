# -*- coding: utf8 -*-

# Created with PyCharm.
# Date: 4/28/14
# Time: 7:58 PM

__author__ = 'redlex'

from Event import Event


class Delegate(object):
    def __init__(self, name):
        self.name = name
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)
        return self

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        return self

    def clear(self):
        self.observers = []

    def notify(self, *args, **kwargs):
        event = Event(self.name, *args, **kwargs)
        for observer in self.observers:
            if callable(observer):
                observer(event)

    __iadd__ = add_observer
    __isub__ = remove_observer
