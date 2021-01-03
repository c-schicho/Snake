"""
Author: Christopher Schicho
Project: Snake
Version: 0.0
"""


class Config:

    # window
    width = 660   # 22 * 30 (grid_size)
    height = 480  # 16 * 30 (grid_size)

    # speed
    speed = 10

    # game surface
    grid_size = 30
    grid_width = width // grid_size
    grid_height = height // grid_size

    # game colors
    surface_color = (70, 70, 70)
    snake_head_color = (20, 200, 20)
    snake_body_color = (20, 170, 20)
    food_color = (200, 150, 50)
    font_color = (255, 255, 255)

    # directions
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)