class Player:

    player_x_change = 0
    player_y_change = 0

    def __init__(self, image):
        self.x = 368
        self.y = 535
        self.image = image

    def play(self, img_player):
        return img_player, (self.x, self.y)



