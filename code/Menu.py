
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.CONST import COLOR_BLUE, COLOR_DARKBLUE, MENU_OPTION, COLOR_WHITE, CONTROLS, COLOR_BLACK


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./Assets/Menu_Background.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load("./Assets/MenuMusic.wav")
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            #Contornos:
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (380, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (385, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (390, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (395, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (415, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (420, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (425, 67))
            self.menu_text(70, 'Ninja', COLOR_DARKBLUE, (395, 67))
            self.menu_text(70, 'Runner', COLOR_DARKBLUE, (415, 120))
            self.menu_text(70, 'Runner', COLOR_DARKBLUE, (420, 120))
            self.menu_text(70, 'Runner', COLOR_DARKBLUE, (425, 120))
            self.menu_text(70, 'Runner', COLOR_DARKBLUE, (380, 120))
            self.menu_text(70, 'Runner', COLOR_DARKBLUE, (385, 120))
            self.menu_text(70, 'Runner', COLOR_DARKBLUE, (390, 120))

            self.menu_text(70, 'Ninja', COLOR_WHITE, (400, 70))
            self.menu_text(70, 'Runner', COLOR_WHITE, (400, 118))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_BLUE, (400, 300 + 65 * i))

                else:
                    pygame.draw.rect(surface=self.surf, color=COLOR_DARKBLUE, rect=(285, 276, 230,50), border_radius=10)
                    pygame.draw.rect(surface=self.surf, color=COLOR_DARKBLUE, rect=(285, 340, 230,50), border_radius=10)
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE,(400, 300 + 65 * i))

            for i in range(len(CONTROLS)):
                self.menu_text(20, CONTROLS[i], COLOR_DARKBLUE, (178, 370 + 30 * i))
                self.menu_text(20, CONTROLS[i], COLOR_WHITE, (180, 370 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # CLose Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("fonts/Ninja Attack Italic.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

