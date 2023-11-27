
# 在屏幕上画图片
def draw_img(surf,img_path,size,x,y):
    import pygame
    if type(size) == tuple:
        img = pygame.image.load(img_path)
        img_rect = img.get_rect()
        img_rect.x = x
        img_rect.y = y
        img_size = pygame.transform.scale(img,(size))
        surf.blit(img_size,img_rect)
    else:
        raise Exception('draw_img : Size type error : not tuple.')