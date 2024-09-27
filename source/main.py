#!/usr/bin/env python3

from utils import scale_x, scale_y, screen, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, clock
from menus import load_high_scores, save_high_scores, update_high_scores, display_high_scores, show_text, draw_pause_overlay
from snake import Snake
from obstacles import generate_obstacles, draw_obstacles, move_random_obstacles
from food import Food
from constants import Colors, Directions, States, Levels
import pygame
import sys

def main():
    high_scores = load_high_scores()
    snake = Snake()
    obstacles = generate_obstacles()
    food = Food(obstacles)
    score = 0
    state = States.MENU
    speed = 10
    CURSOR_HIDE_TIME = 1000
    last_mouse_movement = pygame.time.get_ticks()
    cursor_hidden = False

    print(f"Screen dimensions: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Scaling factors: x={scale_x}, y={scale_y}")
    print(f"Cell size: {CELL_SIZE}")

    while True:
        if pygame.time.get_ticks() - last_mouse_movement > CURSOR_HIDE_TIME and not cursor_hidden:
            pygame.mouse.set_visible(False)
            cursor_hidden = True
        elif pygame.mouse.get_rel() != (0, 0):
            pygame.mouse.set_visible(True)
            last_mouse_movement = pygame.time.get_ticks()
            cursor_hidden = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if state == States.MENU:
                    if event.key == pygame.K_RETURN:
                        state = States.LEVEL_SELECTION
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif state == States.LEVEL_SELECTION:
                    if event.key == pygame.K_1:
                        snake = Snake()
                        obstacles = []
                        food = Food(obstacles)
                        score = 0
                        speed = 10
                        level = Levels.EASY_LEVEL
                        state = States.LOADING
                    if event.key == pygame.K_2:
                        snake = Snake()
                        obstacles = generate_obstacles()
                        food = Food(obstacles)
                        score = 0
                        speed = 15
                        level = Levels.MEDIUM_LEVEL
                        state = States.LOADING
                    if event.key == pygame.K_3:
                        snake = Snake()
                        obstacles = generate_obstacles()
                        food = Food(obstacles)
                        score = 0
                        speed = 20
                        level = Levels.HARD_LEVEL
                        state = States.LOADING
                    if event.key == pygame.K_4:
                        snake = Snake()
                        obstacles = generate_obstacles()
                        food = Food(obstacles)
                        score = 0
                        speed = 25
                        level = Levels.EXPERT_LEVEL
                        state = States.LOADING
                elif state == States.PLAYING and level in [Levels.EASY_LEVEL, Levels.MEDIUM_LEVEL, Levels.HARD_LEVEL, Levels.EXPERT_LEVEL]:
                    if event.key == pygame.K_UP:
                        snake.change_direction(Directions.UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(Directions.DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(Directions.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(Directions.RIGHT)
                elif state == States.GAME_OVER:
                    if event.key == pygame.K_RETURN:
                        snake = Snake()
                        obstacles = generate_obstacles()
                        food = Food(obstacles)
                        score = 0
                        speed = 10
                        state = States.MENU
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if state == States.PLAYING and event.key == pygame.K_ESCAPE:
                    state = States.PAUSE
                elif state == States.PAUSE:
                    if event.key == pygame.K_RETURN:
                        state = States.PLAYING
                    elif event.key == pygame.K_ESCAPE:
                        state = States.GAME_OVER
        if state == States.MENU:
            screen.fill(Colors.BLACK)
            show_text("Snake Game", Colors.WHITE, -250 * scale_y)
            show_text("Press ENTER to choose level", Colors.WHITE, -150 * scale_y)
            show_text("Press ESC to quit", Colors.WHITE, -100 * scale_y)
            show_text("In-Game Controls:", Colors.WHITE, 0)
            show_text("Move Up    -->    Up Arrow", Colors.WHITE, 50 * scale_y)
            show_text("Move Left  -->  Left Arrow", Colors.WHITE, 100 * scale_y)
            show_text("Move Down  -->  Down Arrow", Colors.WHITE, 150 * scale_y)
            show_text("Move Right --> Right Arrow", Colors.WHITE, 200 * scale_y)
            show_text("Pause Game -->      Escape     ", Colors.WHITE, 250 * scale_y)
            pygame.display.flip()
        if state == States.LEVEL_SELECTION:
            screen.fill(Colors.BLACK)
            show_text("Press 1 for EASY difficulty", Colors.WHITE, -250 * scale_y)
            show_text("Speed = 10, NO speed increase, NO obstacles", Colors.WHITE, -200 * scale_y)
            show_text("Press 2 for MEDIUM difficulty", Colors.WHITE, -100 * scale_y)
            show_text("Speed = 15, NO speed increase, YES obstacles", Colors.WHITE, -50 * scale_y)
            show_text("Press 3 for HARD difficulty", Colors.WHITE, 50 * scale_y)
            show_text("Speed = 20, YES speed increase +0.25 per food, YES obstacles", Colors.WHITE, 100 * scale_y)
            show_text("Press 4 for EXPERT difficulty", Colors.WHITE, 200 * scale_y)
            show_text("Speed = 25, YES speed increase +1.0 per food, YES obstacles randomly move per 5 food", Colors.WHITE, 250 * scale_y)
            pygame.display.flip()
        if state == States.LOADING:
            countdown_time = 5
            start_ticks = pygame.time.get_ticks()
            while countdown_time > 0:
                screen.fill(Colors.BLACK)
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds > 1:
                    countdown_time -= 1
                    start_ticks = pygame.time.get_ticks()
                countdown_message = f"Starting new match in {countdown_time}"
                show_text(countdown_message, Colors.WHITE)
                pygame.display.flip()
            state = States.PLAYING
        if state == States.PLAYING and level in [Levels.EASY_LEVEL, Levels.MEDIUM_LEVEL, Levels.HARD_LEVEL, Levels.EXPERT_LEVEL]:
            screen.fill(Colors.BLACK)
            if level == Levels.EXPERT_LEVEL:
                if not snake.move():
                    state = States.GAME_OVER
                for food_position in food.food_list:
                    if snake.body[0] == food_position:
                        snake.grow_snake()
                        food.food_list.remove(food_position)
                        food.food_list.append(food.new_position())
                        score += 1
                        if food.food_eaten_update():
                            move_random_obstacles(obstacles, snake.body, [food_position for food_position in food.food_list])
                        if score % 1 == 0:
                            speed += 1
                for obstacle in obstacles:
                    if snake.body[0] in [(x, y) for x in range(obstacle[0], obstacle[0] + obstacle[2], CELL_SIZE) for y in range(obstacle[1], obstacle[1] + obstacle[3], CELL_SIZE)]:
                        state = States.GAME_OVER
                        break
                snake.draw()
                draw_obstacles(obstacles)
                food.draw()
                show_text(f"Score: {score}", Colors.WHITE, -250 * scale_y)
                pygame.display.flip()
            if level == Levels.HARD_LEVEL:
                if not snake.move():
                    state = States.GAME_OVER
                for food_position in food.food_list:
                    if snake.body[0] == food_position:
                        snake.grow_snake()
                        food.food_list.remove(food_position)
                        food.food_list.append(food.new_position())
                        score += 1
                        if score % 1 == 0:
                            speed += 0.25
                for obstacle in obstacles:
                    if snake.body[0] in [(x, y) for x in range(obstacle[0], obstacle[0] + obstacle[2], CELL_SIZE) for y in range(obstacle[1], obstacle[1] + obstacle[3], CELL_SIZE)]:
                        state = States.GAME_OVER
                        break
                snake.draw()
                draw_obstacles(obstacles)
                food.draw()
                show_text(f"Score: {score}", Colors.WHITE, -250 * scale_y)
                pygame.display.flip()
            if level == Levels.MEDIUM_LEVEL:
                if not snake.move():
                    state = States.GAME_OVER
                for food_position in food.food_list:
                    if snake.body[0] == food_position:
                        snake.grow_snake()
                        food.food_list.remove(food_position)
                        food.food_list.append(food.new_position())
                        score += 1
                    for obstacle in obstacles:
                        if snake.body[0] in [(x, y) for x in range(obstacle[0], obstacle[0] + obstacle[2], CELL_SIZE) for y in range(obstacle[1], obstacle[1] + obstacle[3], CELL_SIZE)]:
                            state = States.GAME_OVER
                            break
                    snake.draw()
                    draw_obstacles(obstacles)
                food.draw()
                show_text(f"Score: {score}", Colors.WHITE, -250 * scale_y)
                pygame.display.flip()
            if level == Levels.EASY_LEVEL:
                if not snake.move():
                    state = States.GAME_OVER
                for food_position in food.food_list:
                    if snake.body[0] == food_position:
                        snake.grow_snake()
                        food.food_list.remove(food_position)
                        food.food_list.append(food.new_position())
                        score += 1
                snake.draw()
                food.draw()
                show_text(f"Score: {score}", Colors.WHITE, -250 * scale_y)
                pygame.display.flip()
        if state == States.PAUSE:
            draw_pause_overlay()
        if state == States.GAME_OVER:
            screen.fill(Colors.BLACK)
            show_text("Game Over!", Colors.WHITE, -300 * scale_y)
            show_text(f"Score: {score}", Colors.WHITE, -200 * scale_y)
            show_text("Press ENTER to return to Main Menu", Colors.WHITE, -100 * scale_y)
            show_text("Press ESC to quit", Colors.WHITE, -50 * scale_y)
            high_scores = update_high_scores(high_scores, score, level)
            save_high_scores(high_scores)
            display_high_scores(high_scores, level)
            pygame.display.flip()
        clock.tick(speed)

if __name__ == "__main__":
    main()
