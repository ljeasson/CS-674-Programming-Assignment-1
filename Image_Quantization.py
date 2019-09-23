from PGM import PGMImage
from PIL import Image

def quantize_image(path, gray_levels):
    try:  
        with Image.open(path) as image: 
            print("Path:",path," Gray Level:",gray_levels)
            print()

    except IOError: 
        pass

if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/peppers.pgm"):
        quantize_image(img, 128)
        quantize_image(img, 32)
        quantize_image(img, 8)
        quantize_image(img, 2)