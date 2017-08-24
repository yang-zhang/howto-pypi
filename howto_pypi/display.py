import os
import webbrowser


def howto():
    webbrowser.open('file://' + os.path.realpath('docs/howto-pypi.html'))
