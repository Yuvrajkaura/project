pip install pygame
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Player settings
PLAYER_SIZE = 50
PLAYER_COLOR = BLACK
PLAYER_SPEED = 5

# Cheese settings
CHEESE_SIZE = 20
CHEESE_COLOR = YELLOW

# Obstacle settings
OBSTACLE_SIZE = 30
OBSTACLE_COLOR = RED
OBSTACLE_COUNT = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cheese Collector Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Generate random position for cheese
def random_position(size):
    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(0, SCREEN_HEIGHT - size)
    return x, y

# Initial cheese position
cheese_x, cheese_y = random_position(CHEESE_SIZE)

# Generate initial obstacle positions
obstacles = [random_position(OBSTACLE_SIZE) for _ in range(OBSTACLE_COUNT)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED

    # Keep player on screen
    player_x = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - PLAYER_SIZE, player_y))

    # Check for collision with cheese
    if (player_x < cheese_x + CHEESE_SIZE and player_x + PLAYER_SIZE > cheese_x and
        player_y < cheese_y + CHEESE_SIZE and player_y + PLAYER_SIZE > cheese_y):
        cheese_x, cheese_y = random_position(CHEESE_SIZE)
        print("Cheese collected!")

    # Check for collision with obstacles
    for obstacle_x, obstacle_y in obstacles:
        if (player_x < obstacle_x + OBSTACLE_SIZE and player_x + PLAYER_SIZE > obstacle_x and
            player_y < obstacle_y + OBSTACLE_SIZE and player_y + PLAYER_SIZE > obstacle_y):
            print("Hit an obstacle! Game over.")
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Draw cheese
    pygame.draw.rect(screen, CHEESE_COLOR, (cheese_x, cheese_y, CHEESE_SIZE, CHEESE_SIZE))

    # Draw obstacles
    for obstacle_x, obstacle_y in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE))

    # Update screen
    pygame.display.flip()

    # Control frame rate
    clock.tick(30)

pygame.quit()
