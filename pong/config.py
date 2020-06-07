import os

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
green = (36, 102, 38)
red = (255, 0, 0)
yellow = (247, 214, 25)
chroma = (0, 0, 0)

# TEXT SIZES

text_prompt = 30
text_main_title = 60
text_score = 60
text_winner = 64

# TEXT STYLES

style_prompt = {'font_size': 30, 'horizontal': 'center', 'vertical': 'bottom', 'color': white, 'background': 'transparent'}
style_main_title = {'font_size': 60, 'horizontal': 'center', 'vertical': 'middle', 'color': white, 'background': 'transparent'}
style_end_title = {'font_size': 60, 'horizontal': 'center', 'vertical': 'middle', 'color': yellow, 'background': 'transparent'}
style_score = {'font_size': 64, 'horizontal': 'center', 'vertical': 'top', 'color': black, 'background': white}

basepath = os.path.dirname(os.path.realpath(__file__))

# GAME PARAMS

POINTS_TO_WIN = 5
FPS = 180


