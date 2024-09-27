from utils import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, screen
import random
import pygame
from constants import Colors

def generate_obstacles():
    obstacles = []
    max_width = SCREEN_WIDTH // CELL_SIZE
    max_height = SCREEN_HEIGHT // CELL_SIZE

    for _ in range(2):
        obstacle_length = random.randint(4, 10)
        obstacle_x = random.randint(0, max_width - obstacle_length) * CELL_SIZE
        obstacle_y = random.randint(0, max_height - 1) * CELL_SIZE
        obstacles.append((obstacle_x, obstacle_y, obstacle_length * CELL_SIZE, CELL_SIZE))

    for _ in range(2):
        obstacle_length = random.randint(4, 10)
        obstacle_x = random.randint(0, max_width - 1) * CELL_SIZE
        obstacle_y = random.randint(0, max_height - obstacle_length) * CELL_SIZE
        obstacles.append((obstacle_x, obstacle_y, CELL_SIZE, obstacle_length * CELL_SIZE))

    for _ in range(2):
        obstacle_x = random.randint(0, max_width - 4) * CELL_SIZE
        obstacle_y = random.randint(0, max_height - 3) * CELL_SIZE
        obstacles.append((obstacle_x, obstacle_y, 3 * CELL_SIZE, CELL_SIZE))
        obstacles.append((obstacle_x, obstacle_y + CELL_SIZE * 2, CELL_SIZE, 2 * CELL_SIZE))

    for _ in range(2):
        obstacle_x = random.randint(0, max_width - 3) * CELL_SIZE
        obstacle_y = random.randint(0, max_height - 4) * CELL_SIZE
        obstacles.append((obstacle_x, obstacle_y, 3 * CELL_SIZE, CELL_SIZE))
        obstacles.append((obstacle_x + CELL_SIZE, obstacle_y + CELL_SIZE, CELL_SIZE, 3 * CELL_SIZE))

    for _ in range(2):
        obstacle_x = random.randint(0, max_width - 3) * CELL_SIZE
        obstacle_y = random.randint(0, max_height - 3) * CELL_SIZE
        obstacles.append((obstacle_x, obstacle_y, 3 * CELL_SIZE, CELL_SIZE))
        obstacles.append((obstacle_x, obstacle_y + CELL_SIZE, CELL_SIZE, CELL_SIZE))
        obstacles.append((obstacle_x + CELL_SIZE, obstacle_y + CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE))
        obstacles.append((obstacle_x + 2 * CELL_SIZE, obstacle_y + 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    return obstacles

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, Colors.BLUE, obstacle)

def move_random_obstacles(obstacles, snake_body, food_positions):
    moved_obstacles = random.sample(obstacles, min(2, len(obstacles)))
    for obstacle in moved_obstacles:
        obstacles.remove(obstacle)
        def is_valid_position(new_obstacle):
            if new_obstacle[0] < 0 or new_obstacle[0] + new_obstacle[2] > SCREEN_WIDTH or new_obstacle[1] < 0 or new_obstacle[1] + new_obstacle[3] > SCREEN_HEIGHT:
                return False
            if any(snake_segment in [(x, y) for x in range(new_obstacle[0], new_obstacle[0] + new_obstacle[2], CELL_SIZE) for y in range(new_obstacle[1], new_obstacle[1] + new_obstacle[3], CELL_SIZE)] for snake_segment in snake_body):
                return False
            for other_obstacle in obstacles:
                if pygame.Rect(new_obstacle).colliderect(pygame.Rect(other_obstacle)):
                    return False
            for food_position in food_positions:
                if pygame.Rect(new_obstacle).collidepoint(food_position):
                    return False
            return True
        while True:
            new_x = random.randint(0, (SCREEN_WIDTH - obstacle[2]) // CELL_SIZE) * CELL_SIZE
            new_y = random.randint(0, (SCREEN_HEIGHT - obstacle[3]) // CELL_SIZE) * CELL_SIZE
            new_obstacle = (new_x, new_y, obstacle[2], obstacle[3])
            if is_valid_position(new_obstacle):
                obstacles.append(new_obstacle)
                break
            else:
                obstacles.append(obstacle)
                break
