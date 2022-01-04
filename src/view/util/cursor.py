import pygame

normal_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)

def use_default_cursor():
    pygame.mouse.set_cursor(normal_cursor)

def use_hand_cursor():
    pygame.mouse.set_cursor(hand_cursor)