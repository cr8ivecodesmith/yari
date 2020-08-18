Yari
====

A Kivy-based game engine.


One of the problems you'll encounter when using Kivy for game development
is when you have so many objects on screen especially when those objects
are in their own widget.

The approach we are going to take for this engine is to use as little widget as
possible and draw all game objects directly as canvas instructions.


**Main ideas:**

- Has a built-in app (`yari`)
- Game objects (sprites, shapes, etc.) are canvas InstructionGroups
- Will have functions for collision detection on Game objects.
- Easy creation of events and event listeners.
- A nice default color palette.
- Easily attach/detach the keyboard.
- Has built-in runtime stats node (FPS checks)
- Should be easily integrated on any Kivy project.
- Will not force a certain game design pattern.


## Hello world


```
from yari import yari
from yari.ui import Label

yari.add_node(Label('Hello world!'))

yari.run()
```


## Installation

From source:

```
python setup.py install
```


## Documentation

Todo
