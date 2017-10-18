# -*- coding: utf-8 -*-
import os
from PIL import Image
from glob import glob
import numpy as np

class DataSetImporter(object):
    def __init__(self, fold_path, img_size, img_format):
        super(DataSetImporter,self).__init__()
        self.fold_path = fold_path
        self.data_set_matrix = np.empty((0,0))
        self.img_size =img_size
        self.img_format = img_format
        self.data_set_path_list = []
        self.data_set_count = 0

    def read_data_sets(self):
        if not os.path.exists(self.fold_path):
            pass

        self.data_set_path_list = glob('%s/*.%s'%(self.fold_path,self.img_format))
        self.data_set_count = len(self.data_set_path_list)


    def next_batch(self,batch_size):
        # pass
        index_arr = np.random.randint(0, self.data_set_count,size =(1,batch_size))
        selected_data_paths = np.array(self.data_set_path_list)[index_arr]
        # print selected_data_paths[0]
        data_num = 0 
        for data_dir in selected_data_paths[0]:
 
            data_num += 1
            # print(child.decode('gbk'))
            im = Image.open(data_dir)
            # gray_im = im.convert('L')
            resized_gray_im = im.resize(self.img_size)
            data_array = np.array(resized_gray_im) # 将图像数据转换成np数组
            reshaped_data_array = np.reshape(data_array,(1,-1))
            if(data_num == 1): # 读入第一张图片，并设置矩阵列数
                    self.data_set_matrix = np.empty((0,reshaped_data_array.shape[1]))
            self.data_set_matrix = np.row_stack([self.data_set_matrix, reshaped_data_array])
                # resized_gray_im.show()
        # print(self.data_set_matrix.shape)
        self.data_set_matrix = np.true_divide(self.data_set_matrix,255)
        # print('Total count of data: %s'%(data_num))

        return self.data_set_matrix 



if __name__ == "__main__":
    dataset = DataSetImporter('test',(50,50),'jpg')
    dataset.read_data_sets()
    print dataset.data_set_count
    print dataset.next_batch(5).shape
    print dataset.next_batch(5).shape
    # print dataset.data_set_matrix[0]



