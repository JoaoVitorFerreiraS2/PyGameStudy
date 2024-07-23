import pygame.image
from code.Const import SCREEN_WIDTH
class Menu:
    def __init__(self, screen):
        self.screen: pygame.Surface = screen
        self.surf = pygame.image.load('Projeto Da Uninter\\assets\\city.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        #pygame.mixer_music.load(None)
        #pygame.mixer_music.set_volume(0.2)
        #pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Projeto UninterGame", (255,128,0) ,((SCREEN_WIDTH / 2), 70))
            pygame.display.flip()
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font = pygame.font.SysFont(name='Lacida Sans Typerwriter', size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color)
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)   

    

