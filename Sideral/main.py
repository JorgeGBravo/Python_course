import pygame
import player

# Init Paygame
pygame.init()


print(dir)
# Make the scream
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('images/ovni.png')
pygame.display.set_icon(icon)

# Player var
player_x = 368
player_y = 535
player_x_change = 0
player_y_change = 0


# Loop the game
in_execution = True
while in_execution:

    # Change color screen in RGB
    screen.fill((101, 75, 247))

    # Iterate events
    for event in pygame.event.get():

        # Close event
        if event.type == pygame.QUIT:
            in_execution = False

        # Move Left and Right events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.1
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.1

            # Move Up and Down events
            if event.key == pygame.K_UP:
                player_y_change = -0.1
            if event.key == pygame.K_DOWN:
                player_y_change = 0.1

        # Drop arrow event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    # Modify location
    player_x += player_x_change
    player_y += player_y_change

    # Inside screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if player_y <= 10:
        player_y = 10

    elif player_y >= 535:
        player_y = 535

    screen.blit(player.play(player_x, player_y))

    # Update events
    pygame.display.update()
