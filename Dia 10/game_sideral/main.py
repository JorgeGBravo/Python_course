import pygame
import random
import math
from pygame import mixer


# Init Paygame
pygame.init()


# Make the scream
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('images/ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/space800x600.jpg')

# Music
mixer.music.load('sounds/ultimo-minuto-rcn.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Player var
img_player = pygame.image.load('images/cohete.png')
player_x = 368
player_y = 535
player_x_change = 0
player_y_change = 0

# Invader var
alien_movement_speed = 0.2

img_invader = []
invader_x = []
invader_y = []
invader_x_change = []
invader_y_change = []
invaders_quantity = 10
invaders_base_quantity = 10
list_invaders = ['alien', 'alien_b', 'alien_c']

invader = random.randint(0, len(list_invaders)-1)

for e in range(invaders_quantity):
    img_invader.append(pygame.image.load(f'images/aliens/{list_invaders[invader]}.png'))
    invader_x.append(random.randint(0, 736))
    invader_y.append(random.randint(50, 200))
    invader_x_change.append(0.3)
    invader_y_change.append(30)


# Bullet var
img_bullet = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = 0
bullet_x_change = 0
bullet_y_change = 1
visible_bullet = False


# Game over
img_game_over = pygame.image.load('images/game-over.png')
game_over_x = 150
game_over_y = 75

# Count
count_shoot = 0
count_lives = 3
font_shoot = pygame.font.Font('fonts/destructobeambb_bold.ttf', 16)
font_lives = pygame.font.Font('fonts/destructobeambb_bold.ttf', 16)
text_x_shoot = 10
text_y_shoot = 10
text_x_lives = 715
text_y_lives = 10


# View lives
def view_lives(x, y):
    text = font_shoot.render(f'Lives: {count_lives}', True, (255, 255, 255))
    screen.blit(text, (x, y))


# View points
def view_points(x, y):
    text = font_lives.render(f'Score: {count_shoot}', True, (255, 255, 255))
    screen.blit(text, (x, y))


# Shoot bullet
def shoot_bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x + 23, y + 10))


# Player
def player(x, y):
    screen.blit(img_player, (x, y))


# Invader
def invader(x, y, inv):
    screen.blit(img_invader[inv], (x, y))


# Detect collisions
def is_collision(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Over
def game_over(x, y):
    screen.blit(img_game_over, (x, y))


# Loop the game
in_execution = True
while in_execution:
    if invaders_quantity == 0:
        invaders_quantity = invaders_base_quantity * 2
        for e in range(invaders_quantity):
            img_invader.append(pygame.image.load('images/aliens/alien.png'))
            invader_x.append(random.randint(0 , 736))
            invader_y.append(random.randint(50 , 200))
            invader_x_change.append(0.3)
            invader_y_change.append(30)

    # Change color screen in RGB
    # screen.fill((101, 75, 247))

    # Load image in background screen
    screen.blit(background, (0, 0))

    # Iterate events
    for event in pygame.event.get():

        # Close event
        if event.type == pygame.QUIT:
            in_execution = False

        # Move Left and Right events and press tab bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

            if event.key == pygame.K_SPACE:
                shoot_sound = mixer.Sound('sounds/shoot.mp3')
                shoot_sound.play()
                if count_lives <= 0:
                    count_shoot = 0
                    count_lives = 3

                elif not visible_bullet:
                    bullet_y = player_y
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

            # Move Up and Down events
            if event.key == pygame.K_UP:
                player_y_change = -0.5
            if event.key == pygame.K_DOWN:
                player_y_change = 0.5

        # Drop arrow event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    # Modify location player
    player_x += player_x_change
    player_y += player_y_change

    # Inside screen player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if player_y <= 10:
        player_y = 10
    elif player_y >= 535:
        player_y = 535

    # Modify location invader
    for e in range(invaders_quantity):
        invader_x[e] += invader_x_change[e]

    # Inside screen invader
        if invader_x[e] <= 0:
            invader_x_change[e] = alien_movement_speed
            invader_y[e] += invader_y_change[e]
        elif invader_x[e] >= 736:
            invader_x_change[e] = -alien_movement_speed
            invader_y[e] += invader_y_change[e]
        if invader_y[e] >= 575:
            invader_y[e] = 1
        # Collision shoot invader
        collision_shoot = is_collision(invader_x[e], invader_y[e], bullet_x, bullet_y)
        if collision_shoot:
            collision_sound = mixer.Sound('sounds/blast.mp3')
            collision_sound.play()
            bullet_y = player_y
            visible_bullet = False
            count_shoot += 1

            invaders_quantity -= 1

            invader_x[e] = random.randint(0, 736)
            invader_y[e] = random.randint(50, 200)
        invader(invader_x[e], invader_y[e], e)

        # Collision player invader
        collision_player_invader = is_collision(invader_x[e], invader_y[e], player_x, player_y)
        if collision_player_invader:
            collision_sound = mixer.Sound('sounds/blast.mp3')
            collision_sound.play()
            if count_lives >= 1:
                count_lives -= 1
                player_x = 368
                player_y = 535

    # move the bullet
    if bullet_y <= -5:
        # bullet_y = 500
        visible_bullet = False

    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Count lives
    if count_lives == 0:
        game_over(game_over_x, game_over_y)
        pass

    # Activate characters
    view_points(text_x_shoot, text_x_shoot)
    view_lives(text_x_lives, text_y_lives)
    player(player_x, player_y)

    # Update events
    pygame.display.update()
