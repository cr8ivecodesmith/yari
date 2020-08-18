from kivy.core.window import Window

from yari import yari
from yari.layouts import FloatLayout
from yari.ui import Label


# Initialize nodes
label = Label(
    text='Hello world!',
    background_color=(.1, .2, .5, 1),
    angle=30,
    size_hint=(.2, .2),
)
layout = FloatLayout(
    background_color=(.4, .3, .5, 1),
    size=Window.size,
)


# Compose nodes
layout.add_node(label)
yari.add_node(layout)


if __name__ == '__main__':
    yari.run()
