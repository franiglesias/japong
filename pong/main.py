import sys

from app.app import App

# Init game engine

if __name__ == '__main__':
    app = App()
    code = app.run()
    sys.exit(code)
