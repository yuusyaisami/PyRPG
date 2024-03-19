import pygame

class EntityBase():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x * 32, y * 32, 32, 32)