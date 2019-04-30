# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:19:21 2019

@author: ainok
"""
import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt
import glob, os
import re
from pathlib import Path



def createPadding(query, margin):
    #size=np.size(query)
    #query = np.insert(query, w, values=0, axis=1)
    #create horizontal space
    w=query.shape[0]
    x=np.zeros(shape=(w, margin))
    x.fill(255)
    #x.astype(int)
    query = np.hstack((query, x))
    query = np.hstack((x,query))
    
    
    h=query.shape[1]
    y=np.zeros(shape=(margin, h))
    y.fill(255)
    query = np.vstack((query, y))
    query = np.vstack((y,query))

    return query




def clearBorder(img):
    

    #img = np.array([[10, 2], [0, 4], [5, 6]])
    
    w=img.shape[1]
    h=img.shape[0]
    #print(w)
    #print(h)
    for row in range(h):
        if img[row, 0] == 0:
            #print(row)
            cv2.floodFill(img, None, (0, row), 255)
        if img[row, w-1] == 0:
            cv2.floodFill(img, None, (w-1, row), 255)
    
    for col in range(w):
        if img[0, col] == 0:
            cv2.floodFill(img, None, (col, 0), 255)
        if img[h-1, col] == 0:
            cv2.floodFill(img, None, (col, h-1), 255)

    return img

def cutPunctuation(img,wordname_path):
    #plt.imshow(img)
    img = cv2.bitwise_not(img) 
    newX=256
    newY=256
    #plt.figure()
    #plt.imshow(img)
    #img = cv2.resize(img,(int(newX),int(newY)))
    img=img//255
    y=img.sum(axis=0)
    
    #print (y)
    #print(y.shape)
    num=np.size(img,1)
    x = np.arange(num)
    ###print(x.shape)
    ###fig, ax = plt.subplots()
    ###ax.plot(x,y)
    ###plt.show()
    ###plt.figure()
    
    
    #width=np.size(img,0)
    #xc=np.size(img,0)
    #print(width)
    #img = img[0:width, 0:250]
    #plt.imshow(img)
    
    #x = np.array([1,0,2,0,3,0,4,5,6,7,8])
    #print("========")
    
    index=np.where(y == 0)[0]
    #index=np.where(y <= 10)[0]
    
    #print(index)
    len=index.shape[0]
    rev_index=index[::-1]
    #print(len)
    #print("========")
    
   
    
    width=np.size(img,1)
    
    height=np.size(img,0)
    #print(width)
    #print(height)
    
    
    sum_ink=0
    for i in  range(0, len-1):
        #print(i,"++++")
        
        if rev_index[i+1]<rev_index[i]-1: #by pass the contigues zeros that exist
            #print("dif=",rev_index[i]-rev_index[i+1],"index=",i )
            #print(rev_index[i])
            #print(rev_index[i+1])
            
            xc=rev_index[i+1]
            
            imgF = img[0:height, 0:xc]
            
            
            imgT= img[0:height, xc:width]
            half=height/2
            #print('==========')
            #print('half',half)
            #print('xc',xc)
            hprof=imgT.sum(axis=1)
            sumakiarea=hprof.sum()
            hprofIndex=np.where(hprof == 0)
            hprofZerosNum=np.size(hprofIndex,1)
            
            #print('zeros',hprofZerosNum)
            
            #print('==========')
            #if hprofZerosNum-3 >= half:
            if sumakiarea <=90: 
                
                #cut
                
                imgF=255*imgF
                imgF=abs(255-imgF)
                imgReturn=imgF
                
                #plt.figure()
                #plt.imshow(imgF)
                return imgReturn
            else:
                #do not cut
                img=255*img
                img=abs(255-img)
                imgReturn=img
                return imgReturn









def checkDiacritics(img):
    import numpy as np
    import cv2 as cv2
    from matplotlib import pyplot as plt
    from scipy.interpolate import interp1d
    
    img = cv2.bitwise_not(img)
    #print(img)
    newX=256
    newY=256
    #img = cv2.resize(img,(int(newX),int(newY)))
    img=img/255
    y=img.sum(axis=1)



    #num=np.size(img,0)
    step=0.1
    height=np.size(img,0)
    width=np.size(img,1)
    x_data = np.arange(height)/height
    x_interp = np.arange(1,height-1,step)/height
    
    
    x_data=x_data[::-1]
    x_interp=x_interp[::-1]
    #print(y.shape)
    #print(width)
    #print(height)


    f2 = interp1d(x_data, y, kind='cubic')
    
    
    sumf=0
    for x in x_interp:
        if x>0.75: #near the first minima
          sumf=sumf + (f2(x)*step/(height*width))
          # print(x,f2(x))
          
        
    #print(sumf)

    #########plt.plot(y/width, x_data, 'o', f2(x_interp)/width, x_interp, '+')
    #plt.plot(y/width, x_data, 'o')
    #########plt.figure()
    #########plt.imshow(img)
    
    sumf=sumf*1000
    
    if sumf>50:
       return False #if there is not diacritics
    else:
       return True
   
def applyCircleErosion(word_img):
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
    erode_img = cv2.erode(word_img, kernel, iterations=1)
    return erode_img

def applyCircleErosion2(word_img):
    colorvalue = [0, 0, 0]
    enlarge_img= cv2.copyMakeBorder(word_img,10,10,10,10,cv2.BORDER_REPLICATE,value=colorvalue)
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
    erode_img = cv2.erode(enlarge_img, kernel, iterations=1)
    return erode_img

def applyHorizontalErosion(source_img):
    kernel = np.ones((1,9), np.uint8)
    img_erosion = cv2.erode(source_img, kernel, iterations=1)
    return img_erosion

def applyWordSegmentation(img,folder):
    
    
    source_img=img.copy()
    
    #kernel = np.ones((1,9), np.uint8)
    #img_erosion = cv2.erode(source_img, kernel, iterations=1)
    
    img_erosion=applyHorizontalErosion(source_img)
    
    #rect_img=source_img
    _, contours, hierarchy = cv2.findContours(img_erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    for (i, c) in enumerate(contours):
        area = cv2.contourArea(c)
        
        #do not segment the very small contours
        if area < 200:
            # do not save dots and small contours
            continue
        
        if area > 10000:
            # do not save very big contours
            continue
        
        
        
        
        
        
        #print("\tSize of contour %d: %d" % (i, len(c)))
        (x, y, w1, h1) = cv2.boundingRect(c)
        rect_img=cv2.rectangle(source_img, (x, y), (x + w1, y + h1), (0, 255, 0), 1)
       
       
       #here check for  grap missing diacritics 
      
       #crop_img_erosion=img_erosion[y:y+h, x:x+w]
       #cv2.imwrite('test/'+str(i)+'test_er.png',crop_img_erosion)
        
        #crop_img = img[y:y+h, x:x+w]
        
        
        
        ###print(area)
        
        #print('000000000000')
        ###res=checkDiacritics(crop_img)
        
        ###print(res)
        
        #print('test/'+ folder +'/'+str(i)+'test.png')
        ###if res==True:
            ###crop_img = img[y-5:y+h+5, x:x+w]
            
            #cv2.imwrite('test/'+ folder +'/'+str(i)+'test.png',crop_img)
            #yxxx=0
        ###else:
            ###crop_img = img[y-10:y+h+5, x:x+w]
            #yxxx=0
            #cv2.imwrite('test/'+ folder +'/'+str(i)+'test.png',crop_img)
        crop_imgOr = img[y-10:y+h1, x:x+w1]
        
        crop_img=crop_imgOr.copy()
        
        wordname=str(y)+'-'+str(x)+'-'+str(w1)+'-'+str(h1)
        wordname_path='test/'+ folder +'/'+wordname+'.png'
        
       
        
        
        #w2=crop_img.shape[1]
        #h2=crop_img.shape[0]
        
        #for col in range(w2):
            
            #if crop_img[0, col] == 0:
                #cv2.floodFill(crop_img, None, (col, 0), 255)
        
            #if crop_img[h2-1, col] == 0:
                #cv2.floodFill(crop_img, None, (col, h2-1), 255)
        
        
        
        
        
        
        #clean_img=crop_img
        
        
        #==================
        #check these two functions for proper functioning
        clean_img=clearBorder(crop_img)
        #==================
        
        
        
        
        clean_img=cutPunctuation(clean_img,wordname_path)
        
        
        
        
        
        
        
        
        #clean_img=clearBorder(clean_img.astype(int))
        
        #print('test/'+ folder +'/'+wordname+'.png')
        #cv2.imwrite('test/'+ folder +'/'+str(i)+'test.png',clean_img)
        cv2.imwrite('test/'+ folder +'/'+wordname+'.png',clean_img)
    #rspimg = cv2.resize(oriimg,(int(newX),int(newY)))    
    cv2.imwrite('results/'+folder+'___rects.png',rect_img)
    cv2.imwrite('results/'+folder+'___erosion.png',img_erosion)
    contours_img=cv2.drawContours(img, contours, -1, (0,255,0), 1)
    cv2.imwrite('results/'+folder+'___contours.png',contours_img)   
    


def searchData(query,folder):
    
    
    
    page=[]
    
    #query=createPadding(query, 20) 
    erodeimg=applyCircleErosion(query)
    
    
    #Get the contour of query image
    _, QueryContours, _ = cv2.findContours(erodeimg, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
    #queryContour=cv2.drawContours(query, contours, 1, (0,255,0), 1)    
    count=0
     
    for filename in glob.glob("test/"+folder+"/*.png"):
         
        #print(Path(filename))
        data = cv2.imread(filename,0)
        #Apply erosion to image file
        #data=createPadding(data, 20)
        erodedata=applyCircleErosion(data)
        #Get the contour of image file
        _, DataContours, _ = cv2.findContours(erodedata, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
        
        #cnt = sorted(DataContours, key=cv2.contourArea)
        
        #Check if contours are more than one, we need the second largest contour
        if len(DataContours)>1:
            #print(len(DataContours))
            #Calculate HU moments and compare
            ret = cv2.matchShapes(QueryContours[1],DataContours[1],3,0.0)
            #First filtering with Hu moments
            if ret<0.1:
                area = cv2.contourArea(DataContours[1])
                #print(area)
                #print(filename)
                #Calculate shape context and compare
                sd = cv2.createShapeContextDistanceExtractor()
                
                try:
                    abc = sd.computeDistance(QueryContours[1],DataContours[1])
                except:
                    print(area)
                    print(filename)
                
                if abc<0.06:
                    count=count+1
                    #plt.figure()
                    #plt.imshow(erodedata)
                    #plt.imshow(data)
                    print(filename)
                    print('ContoursNum:',len(DataContours))
                    print('ShapeMatch:',ret)
                    
                    
                    print('Area:',area)
                    print('Context:',abc)
                    (x, y, w, h) = cv2.boundingRect(DataContours[1])
                    print('Width:',w)
                    print('====================')
                    
                    OSfilename=Path(filename)
                    page.append(OSfilename)
                    
                    
                    
                    
                    
                    
        else:
            #print(filename)
            x=0
        #filename='test429.png'
        #oriimg = cv2.imread(filename,0)
    print(count)
     
    return page
  
def createView():
    import re
    #f=open("results/results.html", "r")
   # file_contents = f.read()
   # print( file_contents)
    
    #str = "The rain in Spain"
    #x = re.sub("\\", "/", file_contents)
   # x = file_contents.replace('\\', '/')
   # 
   # f.close()
   
    f=open("results/results.html", "r")
    content=''
    for line in f.readlines():
        print(line)
        x = line.replace('\\', '/')
        x = x.replace('\n', '')
        #f.write(x)
        print(x)
        
        #content=content+'<a href=../'+x+'>'+x+'</a><br>'+'\n'
        content=content+'<a href=../'+x+'>'+x+'</a>'+'<img src=../'+x+'><br>'+'\n'
        f.close()
    print(content)
    f=open("results/results2.html", "w")
    f.write(content)
    f.close()


    
    
    
    
    