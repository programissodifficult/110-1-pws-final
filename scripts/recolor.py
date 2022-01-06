import numpy as np
from pathlib import Path
from os import listdir, path
from PIL import Image

img_folder = 'assets/icons512'
out_folder = f'assets/icons512W'

Path(out_folder).mkdir(exist_ok=True)

for file_name in listdir(img_folder):
    file_path = path.join(img_folder, file_name)
    if path.isfile(file_path):
        img = Image.open(file_path)
        data = np.array(img)

        r1, g1, b1 = 0, 0, 0 # Original value
        r2, g2, b2 = 255, 255, 255 # Value that we want to replace it with

        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:,:,:3][mask] = [r2, g2, b2]

        img = Image.fromarray(data)
        img.save(path.join(out_folder, file_name))