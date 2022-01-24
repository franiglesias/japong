import pygame

from app.exit_code import ExitCode


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.screen = self.set_up_screen(width, height, title)
        self.score_board = None
        self.scenes = []

    @staticmethod
    def set_up_screen(width: int, height: int, title: str):
        pygame.display.set_caption(title)
        return pygame.display.set_mode((width, height))

    def run(self):
        return self.run_or_exit(self.run_scenes())

    def run_or_exit(self, status):
        if status.is_play_again():
            return self.run()
        return status

    def run_scenes(self):
        for scene in self.scenes:
            scene_exit_code = scene.run()
            if scene_exit_code.is_error():
                return scene_exit_code
        return ExitCode(0)

    def add_scene(self, scene):
        self.scenes.append(scene)
