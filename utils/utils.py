from PIL import Image
import numpy as np

def Image2Array(image):
    im_array = np.array(image)
    return im_array

if __name__ == "__main__":
    img = Image.open("img.png")
    print('image size:{}'.format(img.size))
    img2 = img.resize((50,50),Image.ANTIALIAS)
    print('image2 size:{}'.format(img2.size))
    arr =  Image2Array(img)
    print('shape: {}'.format(arr.shape))
    new_arr = arr.reshape(-1,1)
    print('after reshape: {}'.format(new_arr.shape))
