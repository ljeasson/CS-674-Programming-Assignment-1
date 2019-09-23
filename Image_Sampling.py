from PGM import PGMImage
from PIL import Image
import numpy as np
import cv2

def sample_image(path, width, height):
    try:  
        with Image.open(path) as image: 
            #orig_width, orig_height = image.size

            print("Path:",path," Width:",width," Height:",height)
            print()

            image = image.resize((width, height))
            image.show()
            
            #image.save(str(path)+"_new")  

    except IOError: 
        pass

if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/peppers.pgm"):
        sample_image(img, 128, 128)
        sample_image(img, 64, 64)
        sample_image(img, 32, 32)