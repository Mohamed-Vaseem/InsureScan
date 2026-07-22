from PIL import Image

DISPLAY_SIZE = (450, 320)

def load_image(path):
    image = Image.open(path)
    image.thumbnail(DISPLAY_SIZE)
    return image