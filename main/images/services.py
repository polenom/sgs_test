from PIL import Image
from collections import Counter


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def get_predominant_color(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    dominant_color = Counter(pixels).most_common(1)[0][0]
    return rgb_to_hex(dominant_color)


def get_average_color(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    average_color = tuple(int(sum(c) / len(c)) for c in zip(*pixels))
    return rgb_to_hex(average_color)


def get_palette_color(image_path, num_colors=10):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    color_counter = Counter(pixels)
    return [(rgb_to_hex(rgb_color), count) for rgb_color, count in color_counter.most_common(num_colors)]
