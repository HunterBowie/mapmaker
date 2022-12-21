import pygame, windowgui, constants, managers, assets

pygame.init()

window = windowgui.Window(constants.SCREEN_SIZE)
pygame.display.set_caption("Map Maker")

assets.convert_images()

window.set_manager(managers.MainMenu(window))
window.start(auto_cycle=True)