from kivy.core.window import Window

from yari import yari
from yari.graphics import Canvas, Sprite


kb = yari.keyboard
kb.attach()


canvas = Canvas(is_broadcasting=False)

ww, wh = Window.size
s = Sprite(source='Mons 1.png', scale=.2)
s2 = Sprite(source='Mons 2.png', scale=.4)
s.pos = (ww / 2 - s.width / 2, wh / 2 - s.height / 2)
canvas.add(s2)
canvas.add(s)


yari.add_node(canvas)


@kb.listen('on_key_down')
def keys(node, *args):
    if kb.is_key_down('q'):
        s.flip_h = True

    if kb.is_key_down('w'):
        s.flip_v = True

    if kb.is_key_down('o'):
        s.angle += 10
    if kb.is_key_down('p'):
        s.angle -= 10

    if kb.is_key_down('1'):
        s.show()
    if kb.is_key_down('2'):
        s.hide()

    if kb.is_key_down('t'):
        s.source = 'Mons 2.png'
        print(f'POS: {s.size}')

    if kb.is_key_down('c'):
        s.source = 'Mons 1.png'
        s.pos = (ww / 2 - s.width / 2, wh / 2 - s.height / 2)
        s.flip_h = False
        s.flip_v = False


@yari.mainloop.listen('on_timeout')
def update(node, delta):

    if kb.is_key_down('left'):
        s.x -= 400 * delta
    if kb.is_key_down('right'):
        s.x += 400 * delta
    if kb.is_key_down('up'):
        s.y += 400 * delta
    if kb.is_key_down('down'):
        s.y -= 400 * delta

    if kb.is_key_down('z'):
        s.scale += 1 * delta
        print(f'ORIGIN: {s.origin}')
        print(f'POS: {s.pos}')
    if kb.is_key_down('x'):
        s.scale -= 1 * delta
        print(f'ORIGIN: {s.origin}')
        print(f'POS: {s.pos}')

    if kb.is_key_down('escape'):
        kb.detach()


if __name__ == '__main__':
    yari.run()
