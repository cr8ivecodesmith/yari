from kivy.app import App
from kivy.lang import Builder

from yari.core import Root


Builder.load_file('my.kv')


class MyRoot(Root):
    pass


root = MyRoot()


class MyApp(App):

    def build(self):
        return root


if __name__ == '__main__':
    MyApp().run()
