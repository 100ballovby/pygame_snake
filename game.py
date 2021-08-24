import pygame as pg
from objects import GameRound, Snake, Food

game = GameRound()
snake = Snake()
food = Food(game.colors['green'],
            game.screen_width,
            game.screen_height)

game.check_errors()
game.set_title('Snake game')

while True:
    snake.change_to = game.event_loop(snake.change_to)  # определяю, куда поворачиваться
    snake.validate_direction()  # проверяю, можно ли поворачиваться
    snake.change_head_position()  # поворачиваюсь

    game.score, food.food_pos = snake.body_mechanism(
        game.score, food.food_pos, game.screen_width, game.screen_height
    )

    snake.draw_snake(game.play_surface, game.colors['white'])
    food.draw_food(game.play_surface)

    snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()


