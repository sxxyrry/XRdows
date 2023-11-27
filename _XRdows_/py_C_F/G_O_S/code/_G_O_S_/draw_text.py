import pathlib
import os

folder = pathlib.Path(__file__).parent.resolve()

font_file = os.path.join(folder,'./py_C_F/font/simkai.ttf')

# 在屏幕上画文字
def draw_text(surf, text, size, color, x, y):
    import pygame
    if type(size) == tuple:
        font = pygame.font.Font(font_file, size[0])
        text_surface = font.render(text, True, color, (0, 0, 0, 0))  # 添加透明度参数
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surface, text_rect)
    else:
        raise Exception("draw_text : Size type error : not tuple.")