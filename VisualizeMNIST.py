import gzip
import struct
from PIL import Image

input_path = "./Mnist_data/train-images-idx3-ubyte.gz"
dump_path = "./VisualizedData/"

def main():
    with gzip.open(input_path,'r') as f:
        data = f.read()
    fmt = '>4I'
    magic, num, row, col = struct.unpack_from(fmt,data)
    print magic, num, row, col
    offset = struct.calcsize(fmt)
    
    for i in xrange(num):
        image_size = row * col
        fmt_img = '>%sB' % image_size
        im = Image.new('L', (row, col))  
        img = struct.unpack_from(fmt_img, data, offset)
        offset += struct.calcsize(fmt_img)
        im.putdata(img)  
        im.save(dump_path +"%05d" % i+'.png')
        if i%1000 ==0:
            print "dumped %d image from mnist"%i

    print "dumped %d image from mnist"%i         
    print "dump finished"


if __name__ == "__main__":
    main()
   
    

