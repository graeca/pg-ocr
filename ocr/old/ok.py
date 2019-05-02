
    
    
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os



#!wget "https://i.kinja-img.com/gawker-media/image/upload/s--HqfzgkTd--/c_scale,f_auto,fl_progressive,q_80,w_800/wp2qinp6fu0d8guhex9v.jpg"
#!rm sample_data

img = cv2.imread("13.png")
img_cvt=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_cvt)
plt.show()


h=5
for i in range(h):
    print('num',i)