from yari import yari


kb = yari.keyboard
kb.attach()


@kb.listen('on_key_down')
def keys(node, key, modifiers):

    print(f'KEYBOARD - KEY:{key} (MOD:{modifiers})')

    if kb.is_key_down('escape'):
        kb.detach()
        print('Press ESC again to exit.')


if __name__ == '__main__':
    yari.run()
