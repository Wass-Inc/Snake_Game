from constants import Colors
from utils import screen, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
import random
import pygame

class Food:
    def __init__(self, obstacles):
        self.obstacles = obstacles
        self.food_list = [self.new_position() for _ in range(10)]
        self.food_eaten = 0

    def new_position(self):
        while True:
            position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                        random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            if not any(self.position_in_obstacle(position, obstacle) for obstacle in self.obstacles):
                return position

    @staticmethod
    def position_in_obstacle(position, obstacle):
        obstacle_rect = pygame.Rect(obstacle)
        return obstacle_rect.collidepoint(position)

    def draw(self):
        for food_position in self.food_list:
            pygame.draw.rect(screen, Colors.RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))

    def food_eaten_update(self):
        self.food_eaten += 1
        if self.food_eaten % 5 == 0:
            return True
        return False
