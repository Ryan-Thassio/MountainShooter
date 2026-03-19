#!/usr/bin/python
#-* coding: utf-8 -*-

import pygame

from code.CONST import MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 450))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()