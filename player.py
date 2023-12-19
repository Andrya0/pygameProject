import pygame.sprite
from game import *


class Player(pygame.sprite.Sprite):
    right = True

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('beaver.png')
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 10
        self.rect.y -= 10

    def go_left(self):
        self.change_x = -9
        if (self.right):
            self.flip()
            self.right = False

    def go_right(self):
        self.change_x = 9
        if (not self.right):
            self.flip()
            self.right = True

    def stop(self):
        self.change_x = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
