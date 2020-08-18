from random import randint, choice

from kivy.clock import Clock
from kivy.core.window import Window

from yari import yari
from yari.graphics import Canvas, Rectangle
from yari.graphics.colors import *  # noqa


kb = yari.keyboard
kb.attach()

colors = (
    RED, YELLOW, GREEN, MAROON, SKYBLUE, PURPLE, GOLD, LIME,  # noqa
    ORANGE, BEIGE, BROWN,  # noqa
)
ww, wh = Window.size
canvas = Canvas(is_broadcasting=False)
for _ in range(1024):
    s = Rectangle(
        pos=(randint(0, ww), randint(0, wh)),
        size=(randint(10, 100), randint(10, 100)),
        color=choice(colors)
    )
    canvas.add(s)


yari.add_node(canvas)


@yari.mainloop.listen('on_timeout')
def update(node, delta):
    print(f'FPS: {Clock.get_rfps()}')

    ww, wh = Window.size

    attr = choice(('x', 'y'))

    for s in canvas.get_objects():
        cur = getattr(s, attr)
        setattr(s, attr, cur + randint(-100, 100) * delta)

    if kb.is_key_down('r'):
        for s in canvas.get_objects():
            setattr(s, 'source', choice(colors))
            s.pos = (randint(0, ww), randint(0, wh))
            s.size = (randint(10, 100), randint(10, 100))

    if kb.is_key_down('escape'):
        kb.detach()


if __name__ == '__main__':
    yari.run()
