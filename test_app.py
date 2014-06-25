# -*- coding: utf8 -*-

# Created with PyCharm.
# Date: 4/28/14
# Time: 9:46 PM

__author__ = 'redlex'

from AppEvents import Events
import test_event
import time


def timeit(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("work time {0} sec".format(time.time() - start))
        return result
    return wrap


def module_handler(event):
    print("{0.name} event raised".format(event))


class Worker(object):
    def __init__(self):
        pass

    @timeit
    def run(self):
        Events.send(self, "start_work")
        self.do_some_work()
        Events.send(self, "end_work")

    def do_some_work(self):
        Events.send(self, "hello_bug")
        for x in range(100):
            Events.send(self, "it_works", data=x)


class Watcher(object):
    def __init__(self):
        Events.register("start_work", self.start_handler)
        Events.register("end_work", self.end_handler)
        Events.register("stop", self.stop_handler)
        Events.register("it_works", self.base_handler)
        self.counter = 0

    def start_handler(self, event):
        self.base_handler(event)

    def end_handler(self, event):
        self.base_handler(event)

    def stop_handler(self, event):
        self.base_handler(event)

    def base_handler(self, event, data=None):
        print("{2}:: {1} {0.name} event raised".format(event, self.counter, data))


def main():
    Events.register("test_event_loaded", module_handler)
    job = Worker()
    listener = Watcher()
    job.run()
    del listener
    job.run()
    print("--" * 60)
    Events.send(None, "stop")


if __name__ == "__main__":
    main()
