import pathlib
import time
import os
from .draw_img import draw_img
from .draw_text import draw_text
from .G_O_S_text import caption
from .G_O_S_text import concerning
from .G_O_S_text import concerning_content_1
from .G_O_S_text import concerning_content_2
from .const import *

def __G_O_S__():
    import pygame

    # 初始化
    pygame.init()
    pygame.mixer.init()

    # 窗口标题
    pygame.display.set_caption(caption) # type: ignore

    # 特殊定义
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(mode_size) # type: ignore
    folder = pathlib.Path(__file__).parent.resolve()

    # 开机动画
    B_animation = os.path.join(folder, './py_C_F/Boot_animation.png')
    _Boot_animation_ = True

    def Boot_animation():
        if _Boot_animation_ == False:
            draw_text(screen, '作者：XR，版本：0.2 BETA', (20, 20), COLOR7, 100, 10)
        else:
            time.sleep(0.5)
            draw_img(screen, B_animation, (500, 500), mode_size_one / 3.5, mode_size_two / 7)

    # 主循环变量定义
    run_system = True

    # 主循环
    all_sprites = pygame.sprite.Group()
    while run_system:
        clock.tick(FPS)
        screen.fill(black)
        all_sprites.update()
        all_sprites.draw(screen)
        Boot_animation()
        time.sleep(1)
        _Boot_animation_ = False
        pygame.display.update()

    # 关闭游戏
    pygame.quit()

if __name__ == '__main__':
    __G_O_S__()
