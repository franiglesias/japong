import pygame

quit_event = pygame.event.Event(pygame.QUIT)
any_key_event = pygame.event.Event(pygame.KEYDOWN, unicode="a", key=pygame.K_a, mod=pygame.KMOD_NONE)
p_key_event = pygame.event.Event(pygame.KEYDOWN, unicode="p", key=pygame.K_p, mod=pygame.KMOD_NONE)
