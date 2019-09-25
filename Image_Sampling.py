from PGM import PGMImage
from PIL import Image

def sample_image(path, sampling_factor):
    try:
        with Image.open(path) as image: 
            start = path.find('/')+1
            end = path.find('.')
            name = path[start:end]
            print(name)
            orig_width, orig_height = image.size

            print("Path:",path,\
                  "Width:",orig_width,\
                  "Height:",orig_height)

            image = image.resize((int(orig_width/sampling_factor),\
                                  int(orig_height/sampling_factor)))
            image = image.resize((orig_width, orig_height))
            image.show()
            
            image.save("images/sampled-"+str(sampling_factor)+" "+str(name)+".pgm")  
    except IOError: 
        pass


if __name__ == "__main__":
    for img in ("images/lenna.pgm", "images/peppers.pgm"):
        for sampling_factor in (2, 4, 8):
            sample_image(img, sampling_factor)

