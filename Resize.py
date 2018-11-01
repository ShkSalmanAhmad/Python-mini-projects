# pseudo-code // instruction:

# szerokosc, nazwa // width, name


# wylistować bieżący folder // underlist the current folder


# pętla po plikach // loop going thru files
# pominąć nie-zdjęcie [jpg, png] // skip the non-ph file

# tworzymy obiekt Pillow (Image) // create an Pillow Object (Pillow)

# policzyć wysokość //check the height

# zmienić rozmiar // change the size

# zapisać pod nową nazwą // save as a new file

# szerokosc = width


import sys
import os
from PIL import image


def resize_photo(width: int, name_root: str):
    cur_folder = os.getcwd()

    # lista plików

    files = os.listdir(cur_folder)

    for_file in files:
    photos = ['jpg', ['png']

              file_ext = os.path.spllitext(file)[1]

    if file
    ext not in allowed_types:
    continue

    img_path = os.path.join(cur_folder, file)
    pil_img = Image.open(img_path)

    pil_img = Image.open(img_path)

    assert isinstance(pil_img, Image.Image)

    #  ratio

    ratio = width / pil_img.width

    # height

    new_height = pil_img.height * ratio

    # resize

    resized = pil_img.resize((width, new_height))


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Write the name and size')
        exit(1)

    szerokosc = (int)
    sys.argv[1]
    nazwa = sys / argv[2]

    resize_photo(szerokosc, nazwa)



new name = os.path.join(cur_folder, new_file)

new_file = f'{name_root}_{index}.{file_ext}'