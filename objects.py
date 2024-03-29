import random
import time
import sys
import pygame as pg


class GameRound:
    def __init__(self):
        # screen size
        self.screen_width = 720
        self.screen_height = 460

        self.play_surface = pg.display.set_mode(
            (self.screen_width, self.screen_height)
        )

        # colors
        self.colors = {
            'red': pg.Color(255, 0, 0),
            'green': pg.Color(0, 255, 0),
            'blue': pg.Color(0, 0, 255),
            'white': pg.Color(255, 255, 255),
            'black': pg.Color(0, 0, 0),
        }

        # fps controller
        self.fps_controller = pg.time.Clock()

        # game score
        self.score = 0

    @staticmethod
    def check_errors():
        """
        Initializing pygame and checking for errors.
        If erorr exists, crash program.
        :return: None
        """
        check = pg.init()  # Инициализирую pygame
        if check[1] > 0:  # если есть коды ошибок
            sys.exit()  # закрыть приложение
        else:
            print('OK')

    def set_title(self, title):
        pg.display.set_caption(title)

    def event_loop(self, change_to):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:  # ord('d')
                    change_to = 'RIGHT'
                elif event.key == pg.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pg.K_UP:
                    change_to = 'UP'
                elif event.key == pg.K_DOWN:
                    change_to = 'DOWN'

                elif event.key == pg.K_ESCAPE:  # завершать игру по нажатию на Esc
                    pg.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        pg.display.flip()
        self.fps_controller.tick(23)

    def show_score(self, var=1):
        """
        Displaying score
        :param var: has 2 values. 1 - left corner,
        2 - when game stopped, display score in the center of the screen
        :return:
        """
        score_font = pg.font.SysFont('Calibri', 24)
        score_surface = score_font.render(
            f'Score {self.score}', True, self.colors['black']
        )
        score_rect = score_surface.get_rect()
        if var == 1:
            score_rect.midtop = (80, 10)
        else:
            score_rect.midtop = (360, 230)
        self.play_surface.blit(score_surface, score_rect)

    def game_over(self):
        go_font = pg.font.SysFont('Calibri', 24)
        go_surface = go_font.render(
            'Game Over', True, self.colors['red']
        )
        go_rect = go_surface.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surface, go_rect)
        self.show_score(0)
        pg.display.flip()
        time.sleep(10)
        pg.quit()
        sys.exit()


class Snake:
    def __init__(self):
        self.snake_pos = [100, 0]
        self.snake_body = [[100, 0], [90, 0], [80, 0]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def validate_direction(self):
        if any((
                self.change_to == 'RIGHT' and not self.direction == 'LEFT',
                self.change_to == 'LEFT' and not self.direction == 'RIGHT',
                self.change_to == 'UP' and not self.direction == 'DOWN',
                self.change_to == 'DOWN' and not self.direction == 'UP',
        )):
            self.direction = self.change_to

    def change_head_position(self):
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10
        elif self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        elif self.direction == 'UP':
            self.snake_pos[1] -= 10
        elif self.direction == 'DOWN':
            self.snake_pos[1] += 10

    def body_mechanism(self, score, food_position,
                       screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_pos))
        if (self.snake_pos[0] == food_position[0] and
                self.snake_pos[1] == food_position[1]):
            # если позиция рта змеи и еды совпадает, переместить еду на случайную позицию
            food_position = [
                random.randrange(1, screen_width / 10) * 10,
                random.randrange(1, screen_height / 10) * 10,
            ]
            score += 1
        else:
            self.snake_body.pop()  # удаляю последний сегмент змеи
        return score, food_position

    def draw_snake(self, play_surface, surf_color):
        # displaying segments of snake
        play_surface.fill(surf_color)
        for pos in self.snake_body:
            pg.draw.rect(
                play_surface, (0, 255, 0), pg.Rect(
                    pos[0], pos[1], 10, 10
                )
            )

    def check_for_boundaries(self, game_over, screen_width, screen_height):

        if any((self.snake_pos[0] > screen_width - 10
                or self.snake_pos[0] < 0,
                self.snake_pos[1] > screen_height - 10
                or self.snake_pos[1] < 0)):
            game_over()
        for block in self.snake_body[1:]:
            if block[0] == self.snake_pos[0] and \
                    block[1] == self.snake_pos[1]:
                game_over()


class Food:
    def __init__(self, fc, sw, sh):
        self.food_color = fc
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [
            random.randrange(1, sw / 10) * 10,
            random.randrange(1, sh / 10) * 10,
        ]

    def draw_food(self, play_surface):
        pg.draw.rect(
            play_surface, self.food_color, pg.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y
            )
        )


if __name__ == '__main__':
    GameRound.check_errors()
    game = GameRound()
    snake = Snake()
    food = Food()
