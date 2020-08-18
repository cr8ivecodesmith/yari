from pathlib import Path

from kivy.core.window import Window

from yari import yari
from yari.graphics import Canvas, AnimatedSprite


PATH = Path(__file__).absolute().parent

kb = yari.keyboard
kb.attach()


canvas = Canvas(is_broadcasting=False)
ww, wh = Window.size
s = AnimatedSprite(
    source=str(PATH.joinpath('player.atlas')),
    animation='walk',
    animations=('walk', 'up',),
    scale=.5,
)
s.pos = (ww / 2 - s.width / 2, wh / 2 - s.height / 2)
canvas.add(s)


yari.add_node(canvas)


@kb.listen('on_key_down')
def key_down(node, *args):
    if kb.is_key_down('z'):
        s.scale += .25
    if kb.is_key_down('x'):
        s.scale -= .25

    if kb.is_key_down('q'):
        s.angle += 10
    if kb.is_key_down('w'):
        s.angle -= 10

    if kb.is_key_down('escape'):
        kb.detach()

    s.play()


@kb.listen('on_key_up')
def key_up(node, *args):
    s.stop()


@yari.mainloop.listen('on_timeout')
def update(node, delta):

    if kb.is_key_down('left'):
        s.x -= 400 * delta
        s.flip_v = False
        s.flip_h = True
        s.animation = 'walk'
    if kb.is_key_down('right'):
        s.x += 400 * delta
        s.flip_v = False
        s.flip_h = False
        s.animation = 'walk'
    if kb.is_key_down('up'):
        s.y += 400 * delta
        s.flip_v = False
        s.animation = 'up'
    if kb.is_key_down('down'):
        s.y -= 400 * delta
        s.flip_v = True
        s.animation = 'up'


if __name__ == '__main__':
    yari.run()
