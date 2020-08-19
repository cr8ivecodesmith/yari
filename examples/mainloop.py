from yari import yari
from yari.ui import Label


# Update settings
yari.app.title = 'Main Loop'
yari.window.size = (640, 480)
yari.mainloop.delay = 1 / 30
yari.config.set('graphics', 'target_fps', 30)
yari.config.set('kivy', 'log_level', 'debug')


# Initialize nodes
label = Label(
    text='Hello world!',
    background_color=(1, .75, .23, 1),
    color=(0, 0, 0, 1),
)
label.pos = (
    yari.window.width / 2 - label.width / 2,
    yari.window.height / 2 - label.height / 2,
)


# Compose nodes
yari.add_node(label)


# Mainloop
@yari.mainloop.listen('on_timeout')
def update(node, delta):
    label.angle += 100 * delta
    yari.log.debug(f'UPDATING ANGLE: {label.angle}')


if __name__ == '__main__':
    yari.run()
