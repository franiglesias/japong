import os
import sys

import pong.app.app

# Init game engine

path = os.getcwd()

if __name__ == '__main__':
    app = pong.app.app.App()
    code = app.run()
    sys.exit(code)
