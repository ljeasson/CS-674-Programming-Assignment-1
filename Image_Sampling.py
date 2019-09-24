from PGM import PGMImage
from PIL import Image
import numpy as np

def sample_image(path, sampling_factor):
    try:  
        with Image.open(path) as image: 
            orig_width, orig_height = image.size

            print("Path:",path," Width:",orig_width," Height:",orig_height)
            print()

            image = image.resize((int(orig_width/sampling_factor), int(orig_height/sampling_factor)))
            image = image.resize((orig_width, orig_height))
            image.show()
            
            image.save("images/new_"+str(sampling_factor)+".pgm")  

    except IOError: 
        pass


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/peppers.pgm"):
        sample_image(img, 2)
        sample_image(img, 4)
        sample_image(img, 8)