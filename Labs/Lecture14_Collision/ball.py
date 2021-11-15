import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0

    def get_bb(self):
        # fill here
        return 0,0,0,0

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    #fill here for def stop


# fill here
# class BigBall