from PIL import Image
from PIL import ImageDraw
import colorsys
# import aggdraw

width = 1280
height = 720
background_color_rgb = (255,127,80)

def convert_rgb_to_hls(tuple_color_rgb):
    '''
    Convert rgb color tuple to hls color tuple
    @Param
    RGB color tuple

    @Returns
    HLS color tuple
    '''
    red, green, blue = [color/255.0 for color in tuple_color_rgb ]
    h, l, s = colorsys.rgb_to_hls(red, green, blue)
    return (h, l, s)

def complementary_color(tuple_color_rgb):
    '''
    Calculates a complentary color given an input color
    @Param rgb color tuple
    @Returns rgb color tuple representing complementary color
    '''
    tuple_color_hls = convert_rgb_to_hls(tuple_color_rgb)
    hue, lum, sat = tuple_color_hls
    hue = hue + 0.5
    if hue > 1:
        hue -= 1
    r, g, b = [int(x*255) for x in colorsys.hls_to_rgb(hue, lum, sat)]
    return (r, g, b)


img = Image.new(mode = "RGB", size = (width, height), color = background_color_rgb)

fill_color = complementary_color(background_color_rgb)
draw = ImageDraw.Draw(img, mode="RGBA")

circle_diameter = width/2
start_y = (height - circle_diameter)/2
start_x = (width - circle_diameter)/2
end_y = start_y + circle_diameter
end_x = start_x + circle_diameter

draw.arc(xy=(start_x, start_y, end_x, end_y), start = 0, end = 360, fill = fill_color, width = 4)

img.show()