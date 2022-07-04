import csv
import math
import os
import numpy as np
from PIL import Image
import cv2

def Encryption_Metrics(path,w,f,bt):
    for filename in f:
        im = cv2.imread(path+'/'+filename)
        if bt != 0:
            im = np.flipud(im)
        ans=getans(im)
        for i,r in enumerate(ans):
            if i%3 == 0:
                channel = "R"
            elif i%3 == 1:
                channel = "G"
            else:
                channel = "B"
            if i>5:
                mode = "DD"
            elif i>2:
                mode = "VD"
            else:
                mode = "HD"
            
            w.writerow([filename,mode,channel+" channel","{:.2f}".format(r[0]),"{:.2f}".format(r[1]),"{:.2f}".format(r[2]),
            "{:.2f}".format(r[3]),"{:.2f}".format(r[4]),"{:.6f}".format(r[5])])
def getans(im):
    HD_R = process(im[:, :, 2], "HD")
    HD_G = process(im[:, :, 1], "HD")
    HD_B = process(im[:, :, 0], "HD")
    VD_R = process(im[:, :, 2], "VD")
    VD_G = process(im[:, :, 1], "VD")
    VD_B = process(im[:, :, 0], "VD")
    DD_R = process(im[:, :, 2], "DD")
    DD_G = process(im[:, :, 1], "DD")
    DD_B = process(im[:, :, 0], "DD")
    return HD_R, HD_G, HD_B, VD_R, VD_G, VD_B, DD_R, DD_G, DD_B
        
        
def process(img,mode):
    H,V = img.shape
    if mode == "HD":
        x = img[0:V, 0:H-1].flatten()
        y = img[0:V, 1:H].flatten()
    elif mode == "VD":
        x = img[0:V-1, 0:H].flatten()
        y = img[1:V, 0:H].flatten()
    else:
        x = img[0:V-1, 0:H-1].flatten()
        y = img[1:V, 1:H].flatten()

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    x_var = np.var(x)
    y_var = np.var(y)

    cov = np.cov(x, y)[0][1]
    cor = cov/float(math.sqrt(x_var*y_var))

    return x_mean, y_mean, x_var, y_var, cov, cor

path = 'Origi_image'
path2 = 'Encry_image'
f_o = os.listdir('Origi_image')
f_e = os.listdir('Encry_image')
with open('Output13.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['ImageName','Mode','Channel','Mean(x)','Mean(y)','VAR(X)','VAR(Y)','COV(X, Y)','Correlation(X,Y)'])
    for bt in range(2):
        Encryption_Metrics(path,w,f_o,bt)
        Encryption_Metrics(path2,w,f_e,bt) 