import os
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
import numpy as np

class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"
    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds
    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)


class ExtractPatches(object):
    def __init__(self, fold_path, patch_size, patch_count):
        super(ExtractPatches, self).__init__()
        self.fold_path = fold_path
        self.patch_size = patch_size
        self.patch_count = patch_count

 

    def extract_patches(self):
        if not os.path.exists(self.fold_path):
            pass
        
        if not os.path.exists("./cropped"):
            os.makedirs("./cropped")
        # else:
        #     os.removedirs("./cropped")
        #     os.makedirs("./cropped")

        data_set_dir = os.listdir(self.fold_path)
        if ".DS_Store" in data_set_dir:
            data_set_dir.remove(".DS_Store")

        img_count = len(data_set_dir)
        cropped_id = 0
        for data_dir in data_set_dir:
            if(data_dir == ".DS_Store"):
                continue
 
            child = os.path.join(self.fold_path,data_dir)
            # print(child.decode('gbk'))
            im = Image.open(child)
            (width,height) = im.size
            if width < self.patch_size or height < self.patch_size:
                break

            for _ in xrange(self.patch_count / img_count):
                x = np.random.randint(0, width - self.patch_size)
                y = np.random.randint(0, height - self.patch_size)
                box = (x,y,self.patch_size+x, self.patch_size+y)
                cropped = im.crop(box)  
                filtered_cropped = cropped.filter(MyGaussianBlur(radius = 3))
                residual = ImageChops.difference(cropped, filtered_cropped)

 
                target = Image.new('RGB',(2 * self.patch_size, self.patch_size))

                target.paste(residual,(0,0,self.patch_size,self.patch_size))
                target.paste(filtered_cropped,(self.patch_size,0, 2* self.patch_size,self.patch_size))

                name = "%d"%cropped_id   +".jpg"
                target.save("./cropped/" + name)
                print("Cropping %d patch"%cropped_id)
                cropped_id += 1



if __name__ == "__main__":
    extractor = ExtractPatches("youhua",128,3000)
    extractor.extract_patches()
 