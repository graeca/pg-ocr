# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:55:15 2019

@author: ainok
"""
import cv2 as cv2  
from matplotlib import pyplot as plt
import numpy as np

from segmentation import clearBorder
from segmentation import checkDiacritics
from segmentation import cutPunctuation
from segmentation import applyCircleErosion
from segmentation import applyWordSegmentation
from segmentation import searchData
from segmentation import createView


img = cv2.imread("word/qqqq.png",0);
img = cv2.imread("word/ppp.png",0);
img = cv2.imread("word/kkk.png",0);
img = cv2.imread("word/444.png",0);
img = cv2.imread("word/test429.png",0);

#getX=checkDiacritics(img)
#print(getX)
print("---------------------------")
print("111111111111111111111111111")
print("---------------------------")   



import shutil
import glob, os

f=open("results/results.html", "w")
f.write('')
f.close()
y=[]
for filename in glob.glob("source/*pdf300.png"):
    print(filename)
    filename_w_ext = os.path.basename(filename)
    name, extension = os.path.splitext(filename_w_ext)
    print(name)
    folder=name
    
    ###if os.path.exists('test\\'+folder):
         # remove if exists
        ###shutil.rmtree('test\\'+folder)
    
    
        #shutil.rmtree('test\\'+folder)
    ###os.mkdir('test\\'+folder)
        #img = cv2.imread('source/s35-300.png',0)
        #img = cv2.imread('source/s36-300.png',0)
        #img = cv2.imread('source/0030.pdf-300.png',0)
    
    img = cv2.imread(filename,0)
    
    ###applyWordSegmentation(img,folder)
    query= cv2.imread("word/2335test.png",0); 
    query = cv2.imread('word/1249test.png',0)#
    
    erodeQuery=applyCircleErosion(query)
    plt.figure()
    plt.imshow(erodeQuery)
    x=searchData(query,folder)
    for val in x:
        #print(val)
        y.append(val)
    
#createView()    
print(y)
print(len(y))
 






