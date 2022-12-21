import os, windowgui, pygame

CURRENT_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(CURRENT_DIR, "images")
TILES_DIR = os.path.join(IMAGES_DIR, "tiles")

files = os.listdir(TILES_DIR)

IMAGES = {
    "tiles": []
}

for file in files:
    try:
        IMAGES["tiles"].append(windowgui.load_image(file, TILES_DIR, ext=""))
    except pygame.error:
        print(f"Failed to load file: {file}")

def convert_images():
    """coverting of images must be called after the initalization of pygame display"""
    for name,item in IMAGES.items():
        if type(item) is list:
            new_list = []
            for image in item:
                new_list.append(image.convert_alpha())
            IMAGES[name] = new_list
        else:
            IMAGES[name] = item.convert_alpha()