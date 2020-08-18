from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout as KivyFloatLayout
from kivy.uix.label import Label as KivyLabel


Builder.load_file('kivyhello.kv')


class GameRoot(Widget):
    pass


class KivyHelloApp(App):

    def build(self):
        root = GameRoot()

        layout = KivyFloatLayout(
            # background_color=(.1, .2, .1, 1),
            size=Window.size
        )

        Window.bind(size=layout.setter('size'))

        label = KivyLabel(
            text='Hello world!',
            # background_color=(.3, .2, .1, 1),
            # angle=30,
        )

        label.bind(texture_size=label.setter('size'))

        layout.add_widget(label)
        root.add_widget(layout)

        return root


if __name__ == '__main__':

    KivyHelloApp().run()
