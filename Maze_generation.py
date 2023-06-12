import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Maze parameters
maze_width = 60
maze_height = 50
maze = [[0] * maze_width for _ in range(maze_height)]
path_width = 4

# Algorithm variables
visited_cells = 45
stack = [(random.randint(0, maze_width - 1), random.randint(0, maze_height - 1))]

# Initialize Pygame
pygame.init()
screen_width = maze_width * (path_width + 1)
screen_height = maze_height * (path_width + 1)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MAZE")

def randomized_depth_first_search(visited_cells, stack):
    if visited_cells < maze_width * maze_height:
        # Create a set of unvisited neighbors
        neighbors = []

        x, y = stack[-1]
        
        # North neighbor
        if y > 0 and (maze[y - 1][x] & 0x10) == 0:
            neighbors.append((0, -1))
        # East neighbor
        if x < maze_width - 1 and (maze[y][x + 1] & 0x10) == 0:
            neighbors.append((1, 0))
        # South neighbor
        if y < maze_height - 1 and (maze[y + 1][x] & 0x10) == 0:
            neighbors.append((0, 1))
        # West neighbor
        if x > 0 and (maze[y][x - 1] & 0x10) == 0:
            neighbors.append((-1, 0))

        # Are there any neighbors available?
        if neighbors:
            # Choose one available neighbor at random
            dx, dy = random.choice(neighbors)

            # Create a path between the neighbor and the current cell
            if dx == 0:  # Move vertically
                maze[y][x] |= 0x10 | 0x04 * dy
                maze[y + dy][x] |= 0x10 | 0x01 * -dy
            else:  # Move horizontally
                maze[y][x] |= 0x10 | 0x02 * dx
                maze[y][x + dx] |= 0x10 | 0x08 * -dx

            stack.append((x + dx, y + dy))
            visited_cells += 1
        else:
            # No available neighbors, backtrack
            stack.pop()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Algorithm
    randomized_depth_first_search(visited_cells, stack)
        

    # Clear the screen
    screen.fill(BLACK)

    # Draw Maze
    def infilated_fill(path_width):
        for py in range(path_width):
            for px in range(path_width):
                if cell & 0x10:
                    pygame.draw.rect(screen, WHITE,
                                    ((x * (path_width + 1) + px) * path_width,
                                    (y * (path_width + 1) + py) * path_width,
                                    path_width, path_width))
                else:
                    pygame.draw.rect(screen, BLUE,
                                    ((x * (path_width + 1) + px) * path_width,
                                    (y * (path_width + 1) + py) * path_width,
                                    path_width, path_width))

                    
    def infilated_line(path_width):
        for p in range(path_width):
            if cell & 0x04:
                pygame.draw.rect(screen, WHITE,
                    ((x * (path_width + 1) + p) * path_width,
                    (y * (path_width + 1) + path_width) * path_width,
                    path_width, path_width))
            if cell & 0x02:
                pygame.draw.rect(screen, WHITE,
                    ((x * (path_width + 1) + path_width) * path_width,
                    (y * (path_width + 1) + p) * path_width,
                    path_width, path_width))
                                     
    
    
    
    for x in range(maze_width):
        for y in range(maze_height):
            cell = maze[y][x]
            
            # Each cell is inflated by path_width, so fill it in
            infilated_fill(path_width)  

            # Draw passageways between cells
            infilated_line(path_width)

    # Draw Unit - the top of the stack
    top_x, top_y = stack[-1]
    for py in range(path_width):
        for px in range(path_width):
            pygame.draw.rect(screen, GREEN,
                             ((top_x * (path_width + 1) + px) * path_width,
                              (top_y * (path_width + 1) + py) * path_width,
                              path_width, path_width))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
