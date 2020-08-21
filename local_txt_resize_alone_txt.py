import os
import os.path
import sys
import torch
import torch.utils.data as data
import cv2
import numpy as np
txt_path= "/tasks/task1/facedata.txt"
f = open(txt_path,'r')
lines = f.readlines()
isFirst = True
labels = []
words=[]
imgs_path=[]
for line in lines:
    line = line.rstrip()
    if line.startswith('#'):
        if isFirst is True:
            isFirst = False
        else:
            labels_copy = labels.copy()
            words.append(labels_copy)
            labels.clear()
        path = line[2:]
        path = txt_path.replace(txt_path, 'E:\\data\\') + path
        imgs_path.append(path)
    else:
        line = line.split(' ')
        label = [float(x) for x in line]
        labels.append(label)
words.append(labels)

