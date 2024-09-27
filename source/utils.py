import pygame
import os
from constants import baseResolution

os.environ["SDL_AUDIODRIVER"] = "dummy"

pygame.init()

info = pygame.display.Info()

# Set screen dimensions based on detected resolution
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Calculate scaling factor
scale_x = SCREEN_WIDTH / baseResolution.DESIGN_WIDTH
scale_y = SCREEN_HEIGHT / baseResolution.DESIGN_HEIGHT

# Adjust cell size based on the scale, but ensure it's an integer
CELL_SIZE = max(1, int(20 * min(scale_x, scale_y)))

# Adjust font size based on the scale
FONT = pygame.font.Font(None, int(36 * scale_y))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

home_dir = os.path.expanduser("~")
