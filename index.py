import sys, os, pygame, math
from pygame.locals import *

# set up pygame
pygame.init()

# set up screen data
SCREEN_TITLE = "Eraser"

SCREEN_WIDTH = 1024;
SCREEN_WIDTH_HALF = SCREEN_WIDTH / 2;

SCREEN_HEIGHT = 768;
SCREEN_HEIGHT_HALF = SCREEN_HEIGHT / 2;

# set up the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption(SCREEN_TITLE)

# set up the clock
Clock = pygame.time.Clock()

# set up the colors
COLOR_BLACK = (000, 000, 000)
COLOR_WHITE = (255, 255, 255)
COLOR_RED   = (255, 000, 000)
COLOR_GREEN = (000, 255, 000)
COLOR_BLUE  = (000, 000, 255)
COLOR_BROWN = (222, 184, 135)

def blit_mask(source, dest, destpos, mask, maskrect):
    """
    Blit an source image to the dest surface, at destpos, with a mask, using
    only the maskrect part of the mask.
    """
    tmp = source.copy()
    tmp.blit(mask, destpos, special_flags=pygame.BLEND_RGBA_MULT)
    dest.blit(tmp, destpos, dest.get_rect().clip(maskrect))

# set up assets base dir
ASSETS_BASE_DIR = 'assets/dst/'

picture_surface = pygame.image.load(os.path.join(ASSETS_BASE_DIR, 'picture.jpg')).convert_alpha()

mask_surface = pygame.image.load(os.path.join(ASSETS_BASE_DIR, 'mask.png')).convert_alpha()
mask_rect = mask_surface.get_rect()

cover_surface = pygame.Surface((1024, 768)).convert_alpha()
cover_surface.fill(COLOR_BLUE)
cover_rect = cover_surface.get_rect()

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                mask_rect.x = mouse_x - mask_rect.w / 2
                mask_rect.y = mouse_y - mask_rect.h / 2
                if mask_rect.x < 0:
                    mask_rect.x = 0
                if mask_rect.x > SCREEN_WIDTH - mask_rect.w:
                    mask_rect.x = SCREEN_WIDTH - mask_rect.w
                if mask_rect.y < 0:
                    mask_rect.y = 0
                if mask_rect.y > SCREEN_HEIGHT - mask_rect.h:
                    mask_rect.y = SCREEN_HEIGHT - mask_rect.h

                blit_mask(picture_surface, cover_surface, (mask_rect.x, mask_rect.y), mask_surface, mask_rect)

        screen.blit(cover_surface, cover_rect)
        pygame.display.update()

        Clock.tick(60)
