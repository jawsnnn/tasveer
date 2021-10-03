from PIL import Image

width = 400
height = 300

img = Image.new(mode = "RGB", size = (width, height), color = (255,200,200))
img.show()