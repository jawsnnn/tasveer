'''
Provides color utilities
'''
import colorsys
import math
from collections import Sequence

def rgb_validate(int_input):
    '''Validates and returns validated and corrected RGB tuple'''
    if int_input < 0:
        return 0
    if int_input > 255:
        return 255
    else:
        return int_input

class ColorTuple(Sequence):
    def __init__(self):
        self.colors = (0, 0, 0)
    def __init__(self, tuple_colors):
        if isinstance(tuple_colors, tuple) and len(tuple_colors) == 3:
            self.colors = tuple(map(rgb_validate, tuple_colors))
        else:
            return NotImplemented
    
    def __add__(self, other):
        if len(self) != len(other):
            return NotImplemented
        else:
            return ColorTuple(tuple(map(sum, zip(self.colors, other))))
    
    def __getitem__(self, index):
        return self.colors[index]
    def __len__(self):
        return len(self.colors)    
    def get_tuple(self):
        return self.colors

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

def grade_saturation(tuple_color_rgb, step_size, down=True):
    '''
    Changes saturation of original RGB color by step size
    '''
    # Calculate integer steps for each value
    tuple_color_rgb = ColorTuple(tuple_color_rgb)
    if down:
        step = -1
        step_size_r = int(1/(tuple_color_rgb[0]/step_size))
        step_size_g = int(1/(tuple_color_rgb[1]/step_size))
        step_size_b = int(1/(tuple_color_rgb[2]/step_size))
    else:
        step = 1
        step_size_r = int(1/((255-tuple_color_rgb[0]+1)/step_size))
        step_size_g = int(1/((255-tuple_color_rgb[1]+1)/step_size))
        step_size_b = int(1/((255-tuple_color_rgb[2]+1)/step_size))
    list_colors = []
    step_r = step_g = step_b = 1
    for i in range(step_size):
        step_r += 1
        step_g += 1
        step_b += 1
        if step_r == step_size_r:
            tuple_color_rgb = tuple_color_rgb + (step, 0, 0)
            step_r = 0
        if step_g == step_size_g:
            tuple_color_rgb = tuple_color_rgb + (0, step, 0)
            step_g = 0
        if step_b == step_size_b:
            tuple_color_rgb = tuple_color_rgb + (0, 0, step)
            step_b = 0
        list_colors.append(tuple_color_rgb.get_tuple())
    return list_colors