import pygame
import sys
from maze_generation import generate_maze

pygame.init()

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("TerrOut Horror Game Project")

# Load assets
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (20, 20))  # Adjust desired_width and desired_height

monster_image = pygame.image.load("monster.jpeg")
monster_image = pygame.transform.scale(monster_image, (20, 20))  # Adjust desired_width and desired_height

player_rect = player_image.get_rect()
player_speed = 5

clock = pygame.time.Clock()

# Player attributes
player_position = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
player_velocity = [0, 0]
player_jump = False
player_jump_power = -10
player_gravity = 0.5
is_sprinting = False
sprint_multiplier = 2

# Maze constants
MAZE_WIDTH = 20
MAZE_HEIGHT = 15

# Generate the maze
maze_structure = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)

def render_maze():
    for y, row in enumerate(maze_structure):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x * 40, y * 40, 40, 40))  # Render wall cells in white

# Monster attributes
monster_rect = monster_image.get_rect()
monster_speed = 3

def move_monster(player_position):
    dx = player_position[0] - monster_rect.x
    dy = player_position[1] - monster_rect.y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance > 0:
        dx /= distance
        dy /= distance

    monster_rect.x += dx * monster_speed
    monster_rect.y += dy * monster_speed

def main():
    global player_velocity, player_jump, is_sprinting

    monster_position = [400, 300]  # Initial position of the monster

    while True:
        delta_time = clock.tick(FPS) / 1000.0  # Calculate time since last frame in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Player control
        if keys[pygame.K_w]:
            player_velocity[1] -= player_speed
        if keys[pygame.K_s]:
            player_velocity[1] += player_speed
        if keys[pygame.K_a]:
            player_velocity[0] -= player_speed
        if keys[pygame.K_d]:
            player_velocity[0] += player_speed
        if keys[pygame.K_LSHIFT]:
            is_sprinting = True
        else:
            is_sprinting = False

        # Jumping
        if keys[pygame.K_SPACE] and not player_jump:
            player_velocity[1] = player_jump_power
            player_jump = True

        # Apply gravity
        player_velocity[1] += player_gravity

        # Sprinting
        if is_sprinting:
            player_velocity[0] += player_speed * sprint_multiplier * delta_time
            player_velocity[1] *= sprint_multiplier

        # Update player position
        new_player_position_x = player_position[0] + player_velocity[0]
        new_player_position_y = player_position[1] + player_velocity[1]

        # Calculate the grid cell indices based on the new position
        new_cell_x = int(new_player_position_x // 40)
        new_cell_y = int(new_player_position_y // 40)

        # Check if the new cell contains a wall
        if maze_structure[new_cell_y][new_cell_x] == 0:
            player_position[0] = new_player_position_x
            player_position[1] = new_player_position_y

        # Limit player position within the screen bounds
        player_position[0] = max(player_position[0], 0)
        player_position[0] = min(player_position[0], WINDOW_WIDTH - player_rect.width)
        player_position[1] = max(player_position[1], 0)
        player_position[1] = min(player_position[1], WINDOW_HEIGHT - player_rect.height)

        # Set player_rect's position based on player_position
        player_rect.topleft = player_position

        # Monster movement
        move_monster(player_position)  # Pass player's position to the monster's movement function

        # Rendering
        screen.fill(BLACK)
        render_maze()  # Render maze walls
        screen.blit(player_image, player_rect)
        screen.blit(monster_image, monster_rect)  # Render monster

        pygame.display.flip()

if __name__ == "__main__":
    main()

