class baseResolution:
    DESIGN_WIDTH = 1920
    DESIGN_HEIGHT = 1080

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

class Directions:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class States:
    MENU = 0
    LOADING = 1
    PLAYING = 2
    GAME_OVER = 3
    PAUSE = 4
    LEVEL_SELECTION = 5

class Levels:
    EASY_LEVEL = 6
    MEDIUM_LEVEL = 7
    HARD_LEVEL = 8
    EXPERT_LEVEL = 9