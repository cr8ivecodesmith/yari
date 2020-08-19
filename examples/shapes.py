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
for _ in range(128):
    s = Rectangle(
        pos=(randint(0, ww), randint(0, wh)),
        size=(randint(10, 50), randint(10, 50)),
        color=choice(colors)
    )
    canvas.add(s)


yari.add_node(canvas)


@kb.listen('on_key_down')
def key_down(node, *args):
    ww, wh = Window.size
    if kb.is_key_down('1'):
        for _ in range(128):
            s = Rectangle(
                pos=(randint(0, ww), randint(0, wh)),
                size=(randint(10, 50), randint(10, 50)),
                color=choice(colors)
            )
            canvas.add(s)
    if kb.is_key_down('2'):
        count = len(list(canvas.get_objects())) * 2
        for _ in range(count):
            s = Rectangle(
                pos=(randint(0, ww), randint(0, wh)),
                size=(randint(10, 50), randint(10, 50)),
                color=choice(colors)
            )
            canvas.add(s)
    if kb.is_key_down('3'):
        for s in list(canvas.get_objects())[:]:
            canvas.remove(s.name)
    if kb.is_key_down('escape'):
        kb.detach()
        print('Press ESC again to exit.')


@yari.mainloop.listen('on_timeout')
def update(node, delta):
    yari.log.info(
        f'OBJECTS: {len(list(canvas.get_objects()))} '
        f'({len(canvas.canvas.children)}) '
        f'@ {Clock.get_rfps()} FPS'
    )

    if kb.is_key_down('p'):
        ww, wh = Window.size
        attr = choice(('x', 'y'))
        for s in canvas.get_objects():
            cur = getattr(s, attr)
            setattr(s, attr, cur + randint(-100, 100) * delta)


if __name__ == '__main__':
    yari.run()
