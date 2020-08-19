from pathlib import Path

from kivy.core.window import Window

from yari import yari
from yari.graphics import Canvas, Text
from yari.graphics.colors import GOLD


PATH = Path(__file__).absolute().parent

kb = yari.keyboard
kb.attach()

ww, wh = Window.size
canvas = Canvas(is_broadcasting=False)

t = Text(
    text='Hello\nworld!', font_size=100,
    color=GOLD,
    font_name=PATH.joinpath('Xolonium-Regular.ttf').as_posix(),
)
t.pos = (
    Window.width / 2 - t.width / 2,
    Window.height / 2 - t.height / 2,
)


canvas.add(t)

yari.add_node(canvas)


@kb.listen('on_key_down')
def key_down(node, *args):
    if kb.is_key_down('1'):
        t.text = 'Hello'
    if kb.is_key_down('2'):
        t.text += '\nworld!'
    if kb.is_key_down('3'):
        t.text = ''
    if kb.is_key_down('='):
        t.alpha += .25
    if kb.is_key_down('-'):
        t.alpha -= .25
    if kb.is_key_down('up'):
        t.angle += .45
    if kb.is_key_down('down'):
        t.angle -= .45
    if kb.is_key_down('escape'):
        kb.detach()
        print('Press ESC again to exit.')


if __name__ == '__main__':
    yari.run()
