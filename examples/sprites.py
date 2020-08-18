from random import randint, choice

from kivy.clock import Clock
from kivy.core.window import Window

from yari import yari
from yari.graphics import Canvas, Sprite


kb = yari.keyboard
kb.attach()


images = (
    'Mons 1.png', 'Mons 2.png', 'Mons 3.png', 'Mons 4.png',
)
canvas = Canvas(is_broadcasting=False)
ww, wh = Window.size
for _ in range(32):
    s = Sprite(
        source=choice(images),
        scale=.10,
        pos=(randint(0, ww), randint(0, wh)),
    )
    canvas.add(s)


yari.add_node(canvas)


@kb.listen('on_key_down')
def key_down(node, *args):
    ww, wh = Window.size
    if kb.is_key_down('1'):
        for _ in range(32):
            s = Sprite(
                source=choice(images),
                scale=.10,
                pos=(randint(0, ww), randint(0, wh)),
            )
            canvas.add(s)
    if kb.is_key_down('2'):
        count = len(list(canvas.get_objects())) * 2
        for _ in range(count):
            s = Sprite(
                source=choice(images),
                scale=.10,
                pos=(randint(0, ww), randint(0, wh)),
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
    print(f'OBJECTS: {len(list(canvas.get_objects()))} @ {Clock.get_rfps()}')

    if kb.is_key_down('p'):
        ww, wh = Window.size
        attr = choice(('x', 'y'))
        for s in canvas.get_objects():
            cur = getattr(s, attr)
            setattr(s, attr, cur + randint(-100, 100) * delta)


if __name__ == '__main__':
    yari.run()
