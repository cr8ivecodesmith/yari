"""
Colors

Based on Raylib's color palette

"""

__all__ = (
    'OFFWHITE',
    'WHITE',
    'BLACK',
    'RED',
    'GREEN',
    'BLUE',
    'LIGHTGRAY',
    'GRAY',
    'DARKGRAY',
    'LIGHTGREY',
    'GREY',
    'DARKGREY',
    'YELLOW',
    'GOLD',
    'ORANGE',
    'PINK',
    'MAROON',
    'MAGENTA',
    'LIME',
    'DARKGREEN',
    'SKYBLUE',
    'DARKBLUE',
    'PURPLE',
    'VIOLET',
    'DARKPURPLE',
    'BEIGE',
    'BROWN',
    'DARKBROWN',
)


class Color:

    __slots__ = ('_name', '_rgb',)

    def __init__(self, name, r, g, b):
        self._name = name
        self._rgb = (
            round(r / 255, 4),
            round(g / 255, 4),
            round(b / 255, 4),
        )

    def __iter__(self):
        return iter(self._rgb)

    def __len__(self):
        return len(self._rgb)

    def __getitem__(self, i):
        return self._rgb[i]

    def __repr__(self):
        return f'<Color {self._name} rgb={self._rgb}>'

    __str__ = __repr__


OFFWHITE = Color('OffWhite', 245, 245, 245)
WHITE = Color('White', 255, 255, 255)
BLACK = Color('Black', 0, 0, 0)

RED = Color('Red', 230, 41, 55)
GREEN = Color('Green', 0, 228, 48)
BLUE = Color('Blue', 0, 121, 241)

LIGHTGRAY = Color('LightGray', 200, 200, 200)
GRAY = Color('Gray', 130, 130, 130)
DARKGRAY = Color('DarkGray', 80, 80, 80)
LIGHTGREY = Color('LightGrey', 200, 200, 200)
GREY = Color('Grey', 130, 130, 130)
DARKGREY = Color('DarkGrey', 80, 80, 80)

YELLOW = Color('Yellow', 253, 249, 0)
GOLD = Color('Gold', 255, 203, 0)
ORANGE = Color('Orange', 255, 161, 0)

PINK = Color('Pink', 255, 109, 194)
MAROON = Color('Maroon', 190, 33, 55)
MAGENTA = Color('Magenta', 255, 0, 255)

LIME = Color('Lime', 0, 158, 47)
DARKGREEN = Color('DarkGreen', 0, 117, 44)

SKYBLUE = Color('SkyBlue', 102, 191, 255)
DARKBLUE = Color('DarkBlue', 0, 82, 172)

PURPLE = Color('Purple', 200, 122, 255)
VIOLET = Color('Violet', 135, 60, 190)
DARKPURPLE = Color('DarkPurple', 112, 31, 126)

BEIGE = Color('Beige', 211, 176, 131)
BROWN = Color('Brown', 127, 106, 79)
DARKBROWN = Color('DarkBrown', 76, 63, 47)
