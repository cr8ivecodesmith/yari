"""
Testing ground for animated sprite via Kivy Atlas

Approaches:

1) Rectangle.source
2) Image.source
3) Rectangle.texture

- All 3 approaches works
- An Animation Counter needs to control the rate of changing which texture
  to use otherwise the animation won't appear to be "animating".
- The image texture appears stretched when directly using a Rectangle.
- Kivy.uix.Image has image ratio preservation built-in.

"""
from pathlib import Path

from kivy.atlas import Atlas
from kivy.graphics import Rectangle
from kivy.uix.image import Image

from yari import yari
from yari.core import Node


node = Node()
kb = yari.keyboard
kb.attach()


# Rectangle.source
rect = Rectangle(
    source='atlas://player/walk_1'
)

# Image.source
img = Image(
    source='atlas://player/walk_1',
    pos=(100, 0),
)

# Rectangle.texture
PATH = Path(__file__).absolute().parent
sprite_map = Atlas(PATH.joinpath('player.atlas').as_posix())
rect2 = Rectangle(
    texture=sprite_map['walk_1'],
    pos=(200, 0),
)

# Compose the images into the node
node.canvas.add(rect)
node.canvas.add(rect2)
node.add_node(img)

yari.add_node(node)


class AnimCounter:
    time = 0.
    _rate = 5
    tick = 1 / _rate
    frame = 1
    src = 'atlas://player/walk_{}'
    src2 = 'walk_{}'

    @property
    def rate(self): return self._rate

    @rate.setter
    def rate(self, v):
        v = 1 if v < 1 else v
        self._rate = v
        self.tick = 1 / v


actr = AnimCounter()


@kb.listen('on_key_down')
def keys(node, *args):

    if kb.is_key_down('up'):
        actr.rate += 1
        print(f'Animation rate is now: {actr.rate} FPS')

    if kb.is_key_down('down'):
        actr.rate -= 1
        print(f'Animation rate is now: {actr.rate} FPS')

    if kb.is_key_down('escape'):
        print('Press ESC again to exit.')
        kb.detach()


@yari.mainloop.listen('on_timeout')
def update(node, delta):
    actr.time += delta

    if actr.time > actr.tick:
        actr.time -= actr.tick

        rect.source = actr.src.format(actr.frame)
        img.source = actr.src.format(actr.frame)
        rect2.texture = sprite_map[actr.src2.format(actr.frame)]

        actr.frame += 1
        if actr.frame > 2:
            actr.frame = 1


if __name__ == '__main__':
    yari.run()
