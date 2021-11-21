import random

from pico2d import *

import game_framework
import game_world


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 100, 200
        self.speed = 200 # 200 pixel per second

    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x > 1600:
            self.x = 1600
            self.speed = -self.speed
        if self.x < 0:
            self.x = 0
            self.speed = -self.speed



    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        pass


    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

