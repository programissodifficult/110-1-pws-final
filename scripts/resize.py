from genericpath import exists
from PIL import Image
from os import listdir, path
from pathlib import Path

SIZE = 24
img_folder = 'assets/icons512W'
out_folder = f'assets/icons{SIZE}'

Path(out_folder).mkdir(exist_ok=True)

for file_name in listdir(img_folder):
    file_path = path.join(img_folder, file_name)
    if path.isfile(file_path):
        img = Image.open(file_path)

        resized_img = img.resize((SIZE, SIZE))
        resized_img.save(path.join(out_folder, file_name))
