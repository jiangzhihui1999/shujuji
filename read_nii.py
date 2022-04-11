import cv2
import numpy as np
import SimpleITK as sitk
import os
import matplotlib.pyplot as plt
# import nibabel as nib
from PIL import Image
import time


# ct = sitk.ReadImage('./data_set/train\ct/volume-0.nii')
# ct_array = sitk.GetArrayFromImage(ct)
# for i in range(ct_array.shape[0]):
#     ct_img = ct_array[i, :, :]
#     ct_pic = Image.fromarray(ct_img)
#     plt.imshow(ct_pic, cmap='gray')
#     plt.show()

#
# img_savename = 'F:\LITS2017.jpg'
#
# seg = sitk.ReadImage('F:/LITS2017/Training Batch segment/segmentation-121.nii')
# seg_array = sitk.GetArrayFromImage(seg)
# seg_img = seg_array[250,:,:]
# seg_pic = Image.fromarray(seg_img)
#
# pic=sitk.ReadImage('F:/LITS2017.jpg')
# pic_array = sitk.GetArrayFromImage(pic)
# print(pic_array.shape)
# pic = Image.fromarray(pic_array)
# plt.imshow(pic,cmap='gray')
# plt.show()
#
#
#
# #print(np.unique(seg_img))
#
#
#
# plt.imsave(img_savename,ct_pic, cmap = 'gray')


def nii(niifile):
    filename = os.listdir(niifile)
    for i in filename:
        path = os.path.join(niifile, i)
        print(path)
        ct = sitk.ReadImage(path)
        ct_rray = sitk.GetArrayFromImage(ct)
        print(ct_rray.shape)


filepath = r'E:\PythonPY\pythonProject\MICCAI-LITS2017-master\train\ct'
nii(filepath)