# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np

class DataSetImporter(object):
    def __init__(self, fold_path, img_size):
        super(DataSetImporter,self).__init__()
        self.fold_path = fold_path
        self.data_set_matrix = np.empty((0,0))
        self.img_size =img_size

    def read_data_sets(self, count = 1e100):
        if not os.path.exists(self.fold_path):
            pass
        data_set_dir = os.listdir(self.fold_path)
        data_num = 0

        for data_dir in data_set_dir:
            if(data_num > count):
                break
            if(data_dir == ".DS_Store"):
                continue
            data_num += 1
            child = os.path.join(self.fold_path,data_dir)
            print(child.decode('gbk'))
            im = Image.open(child)
            gray_im = im.convert('L')
            resized_gray_im = im.resize(self.img_size)
            data_array = np.array(resized_gray_im) # 将图像数据转换成np数组
            reshaped_data_array = np.reshape(data_array,(1,-1))
            if(data_num == 1): # 读入第一张图片，并设置矩阵列数
                self.data_set_matrix = np.empty((0,reshaped_data_array.shape[1]))
            self.data_set_matrix = np.row_stack([self.data_set_matrix, reshaped_data_array])
            # resized_gray_im.show()
            print(self.data_set_matrix.shape)
        self.data_set_matrix = np.true_divide(self.data_set_matrix,255)
        print('Total count of data: %s'%(data_num))


    def next_batch(self,batch_size):
        # pass
        index_arr = np.random.randint(0, self.data_set_matrix.shape[0],size =(1,batch_size))
        return self.data_set_matrix[index_arr][0]



if __name__ == "__main__":
    dataset = DataSetImporter('test',(1,1))
    dataset.read_data_sets()
    print dataset.next_batch(5).shape
    print dataset.data_set_matrix[0]



