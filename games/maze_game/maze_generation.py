import random

# Example maze generation function using Recursive Backtracking Algorithm
def generate_maze(width, height):
    # Initialize the maze grid with walls
    maze = [[1] * (width * 2 + 1) for _ in range(height * 2 + 1)]

    def carve_path(x, y):
        maze[y][x] = 0  # Carve the current cell
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # Calculate the new cell coordinates
            if 0 <= nx < width * 2 + 1 and 0 <= ny < height * 2 + 1 and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0  # Carve the wall between the current and new cells
                carve_path(nx, ny)  # Recursively carve the path from the new cell

    start_x, start_y = random.randint(0, width - 1) * 2 + 1, random.randint(0, height - 1) * 2 + 1
    carve_path(start_x, start_y)

    # Place the entrance and exit
    maze[1][0] = 0
    maze[height * 2 - 1][width * 2] = 0

    return maze

# Test the maze generation function
maze = generate_maze(10, 10)
for row in maze:
    print("".join(["#" if cell == 1 else " " if cell == 0 else "D" if cell == 2 else "T" for cell in row]))

