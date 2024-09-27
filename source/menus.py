from utils import home_dir, scale_y, screen, FONT, SCREEN_WIDTH, SCREEN_HEIGHT
import json
from constants import Levels, Colors
import pygame


def load_high_scores():
    try:
        with open(f"{home_dir}/high_scores.json", "r") as file:
            high_scores = json.load(file)
    except FileNotFoundError:
        high_scores = {"easy": [], "medium": [], "hard": [], "expert": []}
    return high_scores

def save_high_scores(high_scores):
    with open(f"{home_dir}/high_scores.json", "w") as file:
        json.dump(high_scores, file)

def update_high_scores(high_scores, score, level):
    level_key = {Levels.EASY_LEVEL: "easy", Levels.MEDIUM_LEVEL: "medium", Levels.HARD_LEVEL: "hard", Levels.EXPERT_LEVEL: "expert"}[level]
    if score not in high_scores[level_key]:
        high_scores[level_key].append(score)
        high_scores[level_key].sort(reverse=True)
        high_scores[level_key] = high_scores[level_key][:5]
    return high_scores

def display_high_scores(high_scores, level):
    level_key = {Levels.EASY_LEVEL: "easy", Levels.MEDIUM_LEVEL: "medium", Levels.HARD_LEVEL: "hard", Levels.EXPERT_LEVEL: "expert"}[level]
    scores = high_scores[level_key]
    if scores:
        show_text(f"{level_key.capitalize()} Level High Scores:", Colors.WHITE, 50 * scale_y)
        for i, score in enumerate(scores):
            show_text(f"{i + 1} ----> {score}", Colors.WHITE, (100 + (i * 50)) * scale_y)
    else:
        show_text("No High Scores Yet", Colors.WHITE)

def show_text(text, color, y_offset=0):
    text_surface = FONT.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

def draw_pause_overlay():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(128)
    screen.blit(overlay, (0, 0))
    show_text("Game Paused", Colors.WHITE, -50 * scale_y)
    show_text("Press ENTER to resume", Colors.WHITE, 0)
    show_text("Press ESC to forfeit", Colors.WHITE, 50 * scale_y)
    pygame.display.flip()
