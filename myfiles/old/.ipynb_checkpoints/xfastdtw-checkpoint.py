# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 16:36:39 2019

@author: ainok
"""
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import cv2

from scipy.spatial.distance import euclidean
img = cv2.imread("word/1249test.png",0);
img = cv2.bitwise_not(img)
newX=256
newY=32
img = cv2.resize(img,(int(newX),int(newY)))
img=img/255
y=img.sum(axis=0)
print(y.shape)
num=np.size(img,1)
b = np.arange(num)
print(b.shape)
fig, ax = plt.subplots()
ax.plot(b,y)
plt.show()
plt.figure()

img2= cv2.imread("word/2840test.png",0);
img2 = cv2.bitwise_not(img2)


img2 = cv2.resize(img2,(int(newX),int(newY)))

plt.imshow(img2, cmap='gray')


img2=img2/255
y2=img2.sum(axis=0)
print(y2.shape)
num=np.size(img2,1)
b = np.arange(num)
print(b.shape)
fig, ax = plt.subplots()
ax.plot(b,y2)
plt.show()

from fastdtw import fastdtw
distance, path = fastdtw(y, y2, dist=euclidean)
print(distance)


from dtw import dtw
euclidean_norm = lambda y, y2: np.abs(y - y2)
d, cost_matrix, acc_cost_matrix, path = dtw(y, y2, dist=euclidean_norm)
print(d)


plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.show()







