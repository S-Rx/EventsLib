# -*- coding: utf8 -*-

# Created with PyCharm.
# Date: 4/28/14
# Time: 10:33 PM

__author__ = 'redlex'


class Event(object):
    def __init__(self, sender, name, *args, **kwargs):
        self.sender = sender
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __getattr__(self, item):
        if item in self.kwargs:
            return self.kwargs[item]
        elif item in self.__dict__:
            return self.__dict__[item]
        else:
            raise AttributeError

    def __getitem__(self, item):
        if 0 <= item < len(self.args):
            return self.args[item]
        else:
            raise AttributeError