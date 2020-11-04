import sys

import pong.app.app

# Init game engine

if __name__ == '__main__':
    app = pong.app.app.App()
    code = app.run()
    sys.exit(code)
