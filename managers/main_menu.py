import windowgui, constants, assets
from managers.map_editor import MapEditor

class MainMenu:
    def __init__(self, window):
        self.window = window

    def init_ui(self):
        start_button = windowgui.Button("start", 0, 0, 250, 50,
        top_img=windowgui.Text(0, 0, "Start").surface)
        windowgui.root_rect(constants.SCREEN_SIZE, start_button.rect,
        center_x=True, center_y=True)

        self.window.ui.add(start_button)
    
    def eventloop(self, event):
        if event.type == windowgui.UIEvent.BUTTON_CLICKED:
            if event.ui_id == "start":
                self.window.set_manager(
                    MapEditor(self.window, 
                    {
                    "tile_size": constants.DEFAULT_TILE_SIZE, 
                    "rows": 100, 
                    "cols": 100,
                    }))