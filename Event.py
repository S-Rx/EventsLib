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