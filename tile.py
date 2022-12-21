import pygame, constants


class Tile:
    def __init__(self, row, col, image):
        self.row = row
        self.col = col
        self.image = image

        self.update_scale(constants.DEFAULT_TILE_SIZE)

        self.selected = False
    
    def update_scale(self, tile_size):
        self.pos = self.col*tile_size, self.row*tile_size
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))

    def render(self, screen):
        screen.blit(self.image, self.pos)