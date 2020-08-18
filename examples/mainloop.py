from kivy.core.window import Window

from yari import yari
from yari.ui import Label


# Initialize nodes
label = Label(
    text='Hello world!',
    background_color=(1, .75, .23, 1),
    color=(0, 0, 0, 1),
)
label.pos = (Window.width / 2 - label.width / 2, Window.height / 2)


# Compose nodes
yari.add_node(label)


# Mainloop
@yari.mainloop.listen('on_timeout')
def update(node, delta):
    label.angle += 3


if __name__ == '__main__':
    yari.run()
