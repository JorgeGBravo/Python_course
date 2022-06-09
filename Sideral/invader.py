import random


class Invader:

    alien_movement_speed = 0.2
    invader_x_change = 0.3
    invader_y_change = 30

    def __init__(self, img):
        self.invader_x = random.randint(0, 736)
        self.invader_y = random.randint(50, 200)
        self.img = img

    def play(self, img_player):
        return img_player, (self.x, self.y)
