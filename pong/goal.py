import pygame

import pong.app
import pong.config
import pong.player

GOAL_HIGHLIGHT_IN_SECONDS = 1.5


class Goal(pygame.sprite.Sprite):
    player: pong.player.Player

    def __init__(self, x, player):
        super().__init__()

        self.image = pygame.Surface((10, 580))
        self.image.fill(pong.config.white)

        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = x

        self.remaining = 0
        self.player = player

    def hit(self):
        pong.app.app.sideHit.play()
        self.image.fill(pong.config.red)

        self.remaining = pong.config.FPS * GOAL_HIGHLIGHT_IN_SECONDS

    def update(self):
        if self.remaining > 0:
            self.remaining -= 1
            return
        self.image.fill(pong.config.white)
