import pygame
import sys

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))

# Load assets
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player control
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed

    # Rendering
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    pygame.display.flip()

