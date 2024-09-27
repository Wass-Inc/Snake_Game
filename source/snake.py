from utils import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, screen
from constants import Directions, Colors
import random
import pygame

class Snake:
    def __init__(self):
        self.body = []
        self.direction = random.choice([Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT])
        self.grow = False
        start_x = (SCREEN_WIDTH // CELL_SIZE // 2) * CELL_SIZE
        start_y = (SCREEN_HEIGHT // CELL_SIZE // 2) * CELL_SIZE
        for i in range(5):
            self.body.append((start_x - i * CELL_SIZE, start_y))

    def move(self):
        head = self.body[0]
        x, y = self.direction
        new_head = (head[0] + x * CELL_SIZE, head[1] + y * CELL_SIZE)
        if new_head in self.body[1:] or new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            return False
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def grow_snake(self):
        self.grow = True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, Colors.GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def get_direction_as_string(self):
        direction_map = {Directions.UP: "Up", Directions.DOWN: "Down", Directions.LEFT: "Left", Directions.RIGHT: "Right"}
        return direction_map.get(self.direction, "Unknown")
