"""
Core Event Manager

"""

__all__ = ('Event',)

from collections import defaultdict

from kivy.event import EventDispatcher


class Event(EventDispatcher):

    def __init__(self, is_broadcasting=True, **kwargs):
        self.is_broadcasting = is_broadcasting
        self.event_subscribers = defaultdict(set)
        super().__init__(**kwargs)

    def create_event(self, event_type):
        """Create a new event

        """
        setattr(self, event_type, lambda *args, **kwargs: None)
        self.register_event_type(event_type)

    def destroy_event(self, event_type):
        """Unbinds all event subscribers and unregisters the event.

        """
        for func in self.event_subscribers[event_type][:]:
            self.unsubscribe(event_type, func)
        self.unregister_event_types(event_type)

    def subscribe(self, event_type, func):
        """Subscribe function on an event

        """
        if func not in self.event_subscribers[event_type]:
            kwargs = {event_type: func}
            self.bind(**kwargs)
            self.event_subscribers[event_type].add(func)

    def unsubscribe(self, event_type, func):
        """Unsubscribe a function from an event

        """
        if func in self.event_subscribers[event_type]:
            kwargs = {event_type: func}
            self.unbind(**kwargs)
            self.event_subscribers[event_type].remove(func)

    def broadcast(self, event_type, *args, **kwargs):
        """Dispatch an event

        """
        if not self.is_broadcasting:
            return
        if self.is_event_type(event_type):
            self.dispatch(event_type, *args, **kwargs)

    def listen(self, event_type):
        """A decorator to subscribe a function to an event

        """
        def decorator(func):
            if func not in self.event_subscribers[event_type]:
                kwargs = {event_type: func}
                self.bind(**kwargs)
                self.event_subscribers[event_type].add(func)
            return func
        return decorator
