import os

# COLORS
import pygame.constants


def inc_byte(byte, pct):
    if byte == 0:
        return (pct * 255) / 100

    byte += byte * pct / 100
    if byte > 255:
        byte = 255
    return byte


def dec_byte(byte, pct):
    byte -= byte * pct / 100

    if byte < 0:
        byte = 0
    return byte


def darken(color, pct):
    return dec_byte(color[0], pct), dec_byte(color[1], pct), dec_byte(color[2], pct)


def lighten(color, pct):
    return inc_byte(color[0], pct), inc_byte(color[1], pct), inc_byte(color[2], pct)


black = (0, 0, 0)
white = (255, 255, 255)
green = (36, 102, 38)
dark_green = darken(green, 40)

red = (255, 0, 0)
yellow = (247, 214, 25)
chroma = (0, 0, 0)

net_color = lighten(green, 80)

# TEXT SIZES

text_prompt = 30
text_main_title = 60
text_score = 60
text_winner = 64

# TEXT STYLES

style_prompt = {'font_size': 30, 'horizontal': 'center', 'vertical': 'bottom', 'color': white,
                'background': 'transparent'}
style_main_title = {'font_size': 60, 'horizontal': 'center', 'vertical': 'middle', 'color': white,
                    'background': 'transparent'}
style_end_title = {'font_size': 60, 'horizontal': 'center', 'vertical': 'middle', 'color': yellow,
                   'background': 'transparent'}
style_score = {'font_size': 64, 'horizontal': 'center', 'vertical': 'top', 'color': dark_green,
               'background': 'transparent'}
style_sets = {'font_size': 48, 'horizontal': 'center', 'vertical': 'bottom', 'color': dark_green,
              'background': 'transparent'}

style_config_side = {'font_size': 20, 'horizontal': 'left', 'vertical': 'middle', 'color': white,
                     'background': 'transparent'}
style_config_players = {'font_size': 20, 'horizontal': 'right', 'vertical': 'middle', 'color': white,
                        'background': 'transparent'}

basepath = os.path.dirname(os.path.realpath(__file__))

# GAME PARAMS

POINTS_TO_WIN = 11
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
