import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
from scipy.signal import argrelextrema
from scipy import interpolate
from scipy.interpolate import interp1d
from scipy.signal import correlate
from scipy.stats.stats import pearsonr 
from scipy.signal import find_peaks

def vHist(img):
    
    img=img/255
    y=img.sum(axis=1)
    ymax=max(y)
    y=y/ymax
    y=1-y
    #index=np.where(y == 0)
    num=np.size(img,0)
    x = np.arange(num)
    
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()
    return y


def drawMiddleLine(img2):
    yv=vHist(img2)
    print(len(yv))
    #yv = np.array([1,2,3,4,5,4,3,2,1,2,3,2,1,2,3,4,5,6,5,4,3,2,1])
    # determine the indices of the local maxima
    #maxInd = argrelextrema(yv, np.greater)
    
    maxInd, _ = find_peaks(yv, height=0)
    
    
    
    # get the actual values using these indices
    ymax = yv[maxInd]  # array([5, 3, 6])
    print(ymax)

    maxPoints=np.sort(ymax, axis=0)[::-1]
    print("max=",maxPoints)

    m1=maxPoints[0]
    m2=maxPoints[1]
    Xind1=np.where(yv == m1)
    Xind2=np.where(yv == m2)
    x1=Xind1[0][0]
    x2=Xind2[0][0]
    ym=(x1+x2)//2
    #print(maxInd[0])
    #print(len(maxInd[0]))
    print(x1,x2,ym)
    h=img2.shape[1]
    lineThickness=1
    #img2=cv2.line(img2, (5, ym), (h-5, ym), (0,255,0), lineThickness)
    img2=cv2.line(img2, (0, ym), (h, ym), (0,255,0), lineThickness)
    return img2, ym