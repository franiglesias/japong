import pygame

from config import white


def create_image(width, height, color=white):
    image = pygame.Surface((width, height))
    image.fill(color)
    return image
