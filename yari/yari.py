"""
Main Yari App

"""

__all__ = ('Yari', 'yari',)

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger

from yari.core import Root


Builder.load_string("""
#:import Yari yari
#:import Timer yari.timer
#:import Keyboard yari.keyboard
#:import RuntimeStats yari.tools.RuntimeStats

<Yari>:
    Timer:
        id: mainloop
        node_id: 'mainloop'
        delay: 1 / 60
        autostart: True

    Keyboard:
        id: keyboard

    RuntimeStats:
        id: runtime_stats
""")


class Yari(Root):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.keyboard = self.ids.keyboard
        self.mainloop = self.ids.mainloop
        self.runtime_stats = self.ids.runtime_stats


yari = Yari()


class YariApp(App):

    def build(self):
        return yari


yari.app = YariApp()
yari.window = Window
yari.config = Config
yari.log = Logger


yari.run = lambda: yari.app.run()
