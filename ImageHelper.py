import pygame
from Helper import RESOLUTION

pygame.display.init()
screen = pygame.display.set_mode(RESOLUTION, 0, 32)

BLOCK_TEXTURES = dict(
    normal="Input/Block_Normal.png",
    empty="Input/Block_Empty.png",
    ramp="Input/Block_Ramp.png",
    ramp_alt="Input/Block_Ramp_Alt.png",
    corner="Input/Block_Corner.png",
    corner_inv="Input/Block_Corner_Inv.png",
    water="Input/Water.png"
)

PLAYER_TEXTURES = dict(
    placeholder=pygame.image.load("Input/Player_Placeholder.png").convert_alpha()
)


