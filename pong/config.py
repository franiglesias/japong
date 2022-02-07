import os

# COLORS
import pygame.constants

from utils.color import darken, lighten

width = 800
height = 600
title = 'Japong!'

black = (0, 0, 0)
white = (255, 255, 255)
green = (36, 102, 38)
dark_green = darken(green, 40)

red = (255, 0, 0)
yellow = (247, 214, 25)
chroma = (0, 0, 0)

net_color = lighten(green, 80)

# TEXT STYLES

styles = {
    'prompt': {
        'font_size': 30,
        'horizontal': 'center',
        'vertical': 'bottom',
        'color': white,
        'background': 'transparent'
    },
    'main_title': {
        'font_size': 60,
        'horizontal': 'center',
        'vertical': 'middle',
        'color': white,
        'background': 'transparent'
    },
    'end_title': {
        'font_size': 60,
        'horizontal': 'center',
        'vertical': 'middle',
        'color': yellow,
        'background': 'transparent'
    },
    'score': {
        'font_size': 64,
        'horizontal': 'center',
        'vertical': 'top',
        'color': dark_green,
        'background': 'transparent'
    },
    'sets': {
        'font_size': 48,
        'horizontal': 'center',
        'vertical': 'bottom',
        'color': dark_green,
        'background': 'transparent'
    },
    'config_side': {
        'font_size': 20,
        'horizontal': 'left',
        'vertical': 'middle',
        'color': white,
        'background': 'transparent'
    },
    'config_players': {
        'font_size': 20,
        'horizontal': 'right',
        'vertical': 'middle',
        'color': white,
        'background': 'transparent'
    },
}


base_path = os.path.dirname(os.path.realpath(__file__))

# GAME PARAMS

POINTS_TO_WIN = 5
FPS = 180

# CUSTOM GAME EVENTS

COMPUTER_MOVES_EVENT = pygame.constants.USEREVENT + 1
COMPUTER_MOVES_TIMER_MS = 5

human_side = 'left'

game_mode = 1

computer_speed = 1
human_speed = 2

left_keys = ('w', 's')
right_keys = ('o', 'l')
