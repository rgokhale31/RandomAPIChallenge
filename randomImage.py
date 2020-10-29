
import requests
import json
from PIL import Image
import numpy as np


def create_pixels():
    response = requests.get("https://www.random.org/integers/?num=7200&min=1&max=255&col=3&base=10&format=plain&rnd=new")
    arr = []
    pixel_set = []
    for line in response.text.splitlines():
        arr = line.split('\t')
        pixel = [int(num) for num in arr]
        pixel_set.append(pixel)
    return pixel_set
    
def generate_pixels_for_image():
    pixels_arr = []
    first_half = create_pixels()
    second_half = create_pixels()
    pixels_arr = first_half + second_half
    return pixels_arr
            
def generate_image():
    pixels = generate_pixels_for_image()
    array = np.array(pixels, dtype=np.uint8)

    new_image = Image.fromarray(array)
    new_image = new_image.resize((120, 120))
    new_image.save('final_image.png')
    
generate_image()
