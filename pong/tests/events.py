import pygame
from pygame.event import Event

quit_event = Event(pygame.QUIT)
any_key_event = Event(pygame.KEYDOWN, unicode="a", key=pygame.K_a, mod=pygame.KMOD_NONE)
p_key_event = Event(pygame.KEYDOWN, unicode="p", key=pygame.K_p, mod=pygame.KMOD_NONE)
r_key_event = Event(pygame.KEYDOWN, unicode="r", key=pygame.K_r, mod=pygame.KMOD_NONE)
l_key_event = Event(pygame.KEYDOWN, unicode="l", key=pygame.K_l, mod=pygame.KMOD_NONE)
u_key_event = Event(pygame.KEYDOWN, unicode="u", key=pygame.K_u, mod=pygame.KMOD_NONE)
d_key_event = Event(pygame.KEYDOWN, unicode="d", key=pygame.K_d, mod=pygame.KMOD_NONE)
num_1_key_event = Event(pygame.KEYDOWN, unicode="1", key=pygame.K_1, mod=pygame.KMOD_NONE)
num_2_key_event = Event(pygame.KEYDOWN, unicode="2", key=pygame.K_2, mod=pygame.KMOD_NONE)
