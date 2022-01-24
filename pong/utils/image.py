import pygame

from config import white, chroma


def create_image(width, height, color=white):
    image = pygame.Surface((width, height))
    image.fill(color)
    return image


def create_transparent_image(width, height):
    image = create_image(width, height, chroma)
    image.set_colorkey(chroma)
    return image
