"""
Author: Christopher Schicho
Project: Snake
Version: 0.0
"""

import sys
import pygame
from Snake import Snake
from Food import Food
from Config import Config as cfg


snake = Snake()
food = Food(snake.snake)


class Game:

    def __init__(self):
        # start pygame
        pygame.init()
        self.clock = pygame.time.Clock()

        # window
        self.window = pygame.display.set_mode((cfg.width, cfg.height))
        pygame.display.set_caption("Snake by Christopher Schicho")

        # font
        self.font = pygame.font.SysFont("comicsansms", 30)


    def __check_input__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # input = left
                if event.key == pygame.K_LEFT:
                    snake.snake_turn(cfg.left)

                # input = right
                elif event.key == pygame.K_RIGHT:
                    snake.snake_turn(cfg.right)

                # input = up
                elif event.key == pygame.K_UP:
                    snake.snake_turn(cfg.up)

                # input = down
                elif event.key == pygame.K_DOWN:
                    snake.snake_turn(cfg.down)


    def run_game(self):
        # game loop
        while True:
            surface = pygame.Surface(self.window.get_size())
            surface.fill(cfg.surface_color)
            self.clock.tick(cfg.speed)
            self.__check_input__()
            snake.snake_move()

            # check whether snake reached food or not
            if snake.snake[0] == food.food_coordinates:
                snake.snake_ate_food()
                food.get_food_coordinates(snake.snake)

            # draw objects and display them
            snake.snake_draw(surface)
            food.food_draw(surface)
            self.window.blit(surface, (0,0))
            self.window.blit(self.font.render(f"Score: {snake.score}", 1, cfg.font_color), (10, 15))
            pygame.display.update()



""" Run Game """
if __name__ == "__main__":
    Game().run_game()
