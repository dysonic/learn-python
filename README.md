# Learn Python

Some tutorials from:

* [learnpython.org](https://www.learnpython.org/)

## Getting started


To run a script:

Example: `python hello.py`

Current examples:

`python bin/print.py`
`python src/mygame/game.py`
`python src/mygame/game2.py`
`python src/urllib-example.py`

# Python version

`python -V` or `python --version`

`python -VV` for more info:
Python 3.12.11 (main, Jul 22 2025, 04:27:29) [GCC 10.2.1 20210110]

## Writing packages

See [Modules_and_Packages](https://www.learnpython.org/en/Modules_and_Packages).

Each package in Python is a directory which MUST contain a special file called __init__.py. This file, which can be empty, indicates that the directory it's in is a Python package. That way it can be imported the same way as a module.

`touch src/writing-packages/foo/__init__.py`

The `__init__.py` file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the `__all__` variable like so:


https://realpython.com/python-all-attribute/

import package [as name]
from module import name [as name]
from module import *

If `__init__.py` doesn’t define `__all__`, then nothing happens when you run a wildcard import on the package.
If `__init__.py` defines `__all__`, then the objects listed in it will be imported.
