from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_string("""
#:import Window kivy.core.window.Window
#:import MyRoot kivy_sprite

<MyRoot>:
    Image:
        id: sprite
        source: 'Mons 1.png'
        pos: Window.width / 2 - self.width / 2, Window.height / 2 - self.height / 2


""")  # noqa


class MyRoot(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attach()

    def attach(self):
        self._keyboard = Window.request_keyboard(
            self.detach, self, 'text'
        )
        if self._keyboard.widget:
            pass
        self._keyboard.bind(
            on_key_down=self._on_keyboard_down,
            on_key_up=self._on_keyboard_up,
        )
        self._keys_pressed = set()
        self._kb_ref = None

    def detach(self):
        self._keyboard.unbind(
            on_key_down=self._on_keyboard_down,
            on_key_up=self._on_keyboard_up,
        )
        self._keyboard = None

    def release(self):
        self._kb_ref.release()
        print('Press ESC again to exit.')

    def _on_keyboard_up(self, keyboard, keycode):
        self._kb_ref = keyboard
        key = keycode[1]
        if key in self._keys_pressed:
            self._keys_pressed.remove(key)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self._kb_ref = keyboard
        key = keycode[1]
        self._keys_pressed.add(key)
        return True

    def is_key_pressed(self, key):
        return True if key in self._keys_pressed else False

    def on_kv_post(self, basew):
        self.sprite = self.ids['sprite']

    def mainloop(self, delay):
        self._clock = Clock.schedule_interval(self.update, delay)

    def update(self, delta):

        if self.is_key_pressed('escape'):
            self.release()
            return False

        if self.is_key_pressed('left'):
            self.sprite.x -= 400 * delta

        if self.is_key_pressed('right'):
            self.sprite.x += 400 * delta

        if self.is_key_pressed('up'):
            self.sprite.y += 400 * delta

        if self.is_key_pressed('down'):
            self.sprite.y -= 400 * delta

        if self.is_key_pressed('s'):
            self.sprite.pos = (
                Window.width / 2 - self.sprite.width / 2, Window.height / 2
            )


class KivySpriteApp(App):

    def build(self):
        root = MyRoot()
        root.mainloop(1 / 60)
        return root


if __name__ == '__main__':
    KivySpriteApp().run()
