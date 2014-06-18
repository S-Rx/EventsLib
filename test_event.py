# -*- coding: utf8 -*-

# Created with PyCharm.
# Date: 4/28/14
# Time: 8:10 PM

__author__ = 'redlex'


from Delegate import Delegate
from AppEvents import *

Events.send(None, "test_event_loaded")


class Test(object):
    def __init__(self):
        self.on_work_start = Delegate("_".join(("start", self.__class__.__name__)))
        self.on_work_end = Delegate("_".join(("end", self.__class__.__name__)))

    def work(self):
        self.on_work_start.notify()
        self.do_some_work()
        self.on_work_end.notify()

    def do_some_work(self):
        pass


def on_start_handler(event):
    print("{0.name} event raised".format(event))


def on_end_handler(event):
    print("{0.name} event raised".format(event))


def main():
    test_obj = Test()
    test_obj.on_work_start += on_start_handler
    test_obj.on_work_end += on_end_handler
    test_obj.work()

    test_obj.on_work_end -= on_end_handler
    test_obj.work()
    AppEvents.stop()


if __name__ == "__main__":
    main()
