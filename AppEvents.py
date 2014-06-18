# -*- coding: utf8 -*-

# Created with PyCharm.
# Date: 4/28/14
# Time: 8:38 PM

__author__ = 'redlex'

from threading import Thread
from Queue import Queue
from Event import Event
import weakref


class _WeakRef:
    def __init__(self, item):

        try:
            self.method = weakref.ref(item.im_func)
            self.instance = weakref.ref(item.im_self)

        except AttributeError:
            self.reference = weakref.ref(item)

        else:
            self.reference = None

    def __call__(self):
        if self.reference:
            return self.reference()

        instance = self.instance()

        if not instance:
            return None

        method = self.method()

        return getattr(instance, method.__name__)


class AppEvents(Thread):

    def __init__(self):
        super(AppEvents, self).__init__()
        self.events = Queue()
        self.signals = {}
        self.work = False
        self.register("stop", self.stop)

    def register(self, signal, slot):
        if signal in self.signals:
            self.signals[signal].insert(0, _WeakRef(slot))
        else:
            self.signals[signal] = []
            self.register(signal, slot)

    def add_event(self, event):
        self.events.put(event)

    def send(self, sender, event_id, *args, **kwargs):
        event = Event(sender, event_id, *args, **kwargs)
        self.add_event(event)
        self.events.join()

    def notify(self, event):
        for slot in self.signals.get(event.name, ()):
            if callable(slot()):
                slot()(event, *event.args, **event.kwargs)

    def run(self):
        self.work = True
        while self.work:
            event = self.events.get()
            self.notify(event)
            self.events.task_done()

    def stop(self, event):
        print("stop")
        self.work = False

    __iadd__ = add_event


Events = AppEvents()
Events.start()
