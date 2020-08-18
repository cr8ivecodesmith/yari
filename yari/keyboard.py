"""
Keyboard System

"""

__all__ = ('Keyboard',)

from kivy.core.window import Window

from yari.core import Node


class Keyboard(Node):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_event('on_key_down')
        self.create_event('on_key_up')

        self._is_attached = False

    def attach(self):
        if self._is_attached:
            return

        self._keyboard = Window.request_keyboard(
            self._keyboard_detach, self, 'text'
        )

        if self._keyboard.widget:
            pass

        self._keyboard.bind(
            on_key_down=self._on_keyboard_down,
            on_key_up=self._on_keyboard_up,
        )

        self.keycode = None
        self.modifiers = None

        self._kb_reference = None

        self._keys_down = set()
        self._is_attached = True

    def detach(self):
        if self._kb_reference:
            self._kb_reference.release()

    def is_key_down(self, key):
        return True if key in self._keys_down else False

    def _keyboard_detach(self):
        if not self._is_attached:
            return

        self._keyboard.unbind(
            on_key_down=self._on_keyboard_down,
            on_key_up=self._on_keyboard_up,
        )
        self._keyboard = None
        self._is_attached = False

    def _on_keyboard_up(self, keyboard, keycode):
        self._kb_reference = keyboard
        self.keycode = keycode

        key = keycode[1]

        if key in self._keys_down:
            self._keys_down.remove(key)

        self.broadcast('on_key_up', key)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self._kb_reference = keyboard
        self.keycode = keycode
        self.modifiers = modifiers

        key = keycode[1]

        self._keys_down.add(key)
        self.broadcast('on_key_down', key, modifiers)

        return True
