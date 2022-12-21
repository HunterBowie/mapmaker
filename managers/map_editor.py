import assets, pygame, constants
from tile import Tile

class MapEditor:
    def __init__(self, window, settings):
        self.window = window
        self.settings = settings
        self.tiles = []
        self.offset = 0, 0
    
    def calc_row_col(self, mouse_pos):
        col = (mouse_pos[0]+self.offset[0])//self.settings["tile_size"]
        row = (mouse_pos[1]+self.offset[1])//self.settings["tile_size"]
        return row, col
    
    def eventloop(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if self.settings["tile_size"]+10 <= constants.MAX_TILE_SIZE:
                    self.update_scale(self.settings["tile_size"]+10)
            elif event.button == 5:
                if self.settings["tile_size"]-10 >= constants.MIN_TILE_SIZE:
                    self.update_scale(self.settings["tile_size"]-10)

    def update_scale(self, tile_size):
        self.settings["tile_size"] = tile_size
        for tile in self.tiles:
            tile.update_scale(tile_size)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            row, col = self.calc_row_col(mouse_pos)
            for tile in self.tiles:
                if tile.row == row and tile.col == col:
                    break
            else:
                self.tiles.append(Tile(row, col, assets.IMAGES["tiles"][0]))


        for tile in self.tiles:
            tile.render(self.window.screen)