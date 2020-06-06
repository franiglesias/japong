import pygame


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.title)

        self.score_board = None

        self.scenes = []

    def run(self):
        for scene in self.scenes:
            error = scene.run()
            if error != 0:
                return error
        return 0

    def add_scene(self, scene):
        self.scenes.append(scene)
