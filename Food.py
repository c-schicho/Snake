"""
Author: Christopher Schicho
Project: Snake
Version: 0.0
"""

import random
import pygame
from Config import Config as cfg


class Food:

    def __init__(self, snake):
        # get initial food
        self.food_coordinates = None
        self.get_food_coordinates(snake)


    def get_food_coordinates(self, snake):
        # get random food coordinates
        food_x = random.randint(0, cfg.grid_width - 1) * cfg.grid_size
        food_y = random.randint(0, cfg.grid_height - 1) * cfg.grid_size
        new_food_coordinates = (food_x, food_y)

        # check whether food coordinates are pointing to a free spot
        if new_food_coordinates in snake:
            self.get_food_coordinates(snake)
        else:
            self.food_coordinates = new_food_coordinates


    def food_draw(self, surface):
        # define food rectangle
        rectangle = pygame.Rect((self.food_coordinates[0], self.food_coordinates[1]), (cfg.grid_size, cfg.grid_size))

        # draw food rectangle
        pygame.draw.rect(surface, cfg.food_color, rectangle)