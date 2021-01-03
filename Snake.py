"""
Author: Christopher Schicho
Project: Snake
Version: 0.0
"""

import pygame
from Config import Config as cfg


class Snake:

    def __init__(self):
        # initial state of the snake
        self.length = 3
        self.snake = [(cfg.width // 2, cfg.height // 2),
                      (cfg.width // 2 - cfg.grid_size, cfg.height // 2),
                      (cfg.width // 2 - 2 * cfg.grid_size, cfg.height // 2)]
        self.direction = cfg.right
        self.score = 0



    def __reset__(self):
        # reset state of the snake to initial state
        self.length = 3
        self.snake = [(cfg.width // 2, cfg.height // 2),
                      (cfg.width // 2 - cfg.grid_size, cfg.height // 2),
                      (cfg.width // 2 - 2 * cfg.grid_size, cfg.height // 2)]
        self.direction = cfg.right
        self.score = 0


    def snake_ate_food(self):
        self.length += 1
        self.score += 1


    def snake_turn(self, direction):
        # input direction is the same or the opposite of the snake's direction
        if direction == self.direction or (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        # input direction is not the same or the opposite of the snake's direction
        else:
            self.direction = direction


    def snake_move(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0] * cfg.grid_size, head[1] + self.direction[1] * cfg.grid_size)

        # game ending conditions
        if new_head in self.snake or 0 > new_head[0] or cfg.width < new_head[0] \
                                  or 0 > new_head[1] or cfg.height < new_head[1]:
            self.__reset__()

        # game continuing conditions
        else:
            # insert new head on position 0 in snake
            self.snake.insert(0, new_head)

            # snake is too long
            if len(self.snake) > self.length:
                self.snake.pop()


    def snake_draw(self, surface):
        # draw head of the snake
        head = self.snake[0]
        head_rectangle = pygame.Rect((head[0], head[1]), (cfg.grid_size, cfg.grid_size))
        pygame.draw.rect(surface, cfg.snake_head_color, head_rectangle)

        # draw body of the snake
        for field in self.snake[1:]:
            body_rectangle = pygame.Rect((field[0], field[1]), (cfg.grid_size, cfg.grid_size))
            pygame.draw.rect(surface, cfg.snake_body_color, body_rectangle)