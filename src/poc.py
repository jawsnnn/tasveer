from PIL import Image
from PIL import ImageDraw

from lib.color import complementary_color, grade_saturation

width = 1280
height = 720
background_color_rgb = (161, 111, 221)

img = Image.new(mode = "RGB", size = (width, height), color = background_color_rgb)

fill_color = complementary_color(background_color_rgb)
draw = ImageDraw.Draw(img, mode="RGBA")

circle_diameter = int(width/2)
circle_radius = int(circle_diameter/2)
print(fill_color)
print(circle_radius)
list_colors = grade_saturation(fill_color, 640, down=False, channels = ())
count=0
for i in list_colors:
    count += 1
    print(i, count)
for i in range(640):
    circle_diameter -= 1
    start_y = (height - circle_diameter)/2
    start_x = (width - circle_diameter)/2
    end_y = start_y + circle_diameter
    end_x = start_x + circle_diameter
    draw.arc(xy=(start_x, start_y, end_x, end_y), start = 0, end = 360, fill = list_colors[i], width = 2)
img.show()