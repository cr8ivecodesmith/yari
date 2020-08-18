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
for _ in range(512):
    s = Sprite(
        source=choice(images),
        scale=.10,
        pos=(randint(0, ww), randint(0, wh)),
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
            setattr(s, 'source', choice(images))
            s.pos = (randint(0, ww), randint(0, wh))

    if kb.is_key_down('escape'):
        kb.detach()


if __name__ == '__main__':
    yari.run()
