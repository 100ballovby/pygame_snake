import random
import time
import sys
import pygame as pg


class GameRound:
    # TODO: make a main Game Object.
    def __init__(self):
        pass

    @staticmethod
    def check_errors():
        """
        Initializing pygame and checking for errors.
        If erorr exists, crash programm.
        :return: None
        """
        check = pg.init()  # Инициализирую pygame
        if check[1] > 0:  # если есть коды ошибок
            sys.exit()  # закрыть приложение
        else:
            print('OK')


class Snake:
    # TODO: choose snake position and appearance,
    #  add eating method
    pass


class Food:
    # TODO: initialize food, choose food position
    pass


if __name__ == '__main__':
    GameRound.check_errors()
    game = GameRound()
    snake = Snake()
    food = Food()
