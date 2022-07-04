import csv
import math
import os
import numpy as np
from PIL import Image
import cv2

def Encryption_Metrics(path,path2,w,f,fe):
    no=1
    origin=[]
    encode=[]
    count=0
    for file in f:
        name = str(file)
        origin.append(name)
        count=count+1
    for file in fe:
        name = str(file)
        encode.append(name)
    for i in range(count):
        o = Image.open(path+'/'+origin[i])
        e = Image.open(path2+'/'+encode[i])
        PixelArray_o = np.asarray(o)
        PixelArray_e = np.asarray(e)
        V=0
        H=0
        tf=True
        for n, dim in enumerate(PixelArray_o):
            for num, row in enumerate(dim):
                if(tf):
                    V=V+1
            tf=False
            H=H+1
        final_V=V
        final_H=H
        rgb_o_r = [[0]*V for i in range(H)]
        rgb_e_r = [[0]*V for i in range(H)]
        rgb_o_g = [[0]*V for i in range(H)]
        rgb_e_g = [[0]*V for i in range(H)]
        rgb_o_b = [[0]*V for i in range(H)]
        rgb_e_b = [[0]*V for i in range(H)]
        V=0
        H=0
        for n, dim in enumerate(PixelArray_o):
            for num, row in enumerate(dim):
                r, g, b = row
                rgb_o_r[V][H]=r
                rgb_o_g[V][H]=g
                rgb_o_b[V][H]=b
                V=V+1
            V=0
            H=H+1
        V=0
        H=0
        for n, dim in enumerate(PixelArray_e):
            for num, row in enumerate(dim):
                r, g, b = row
                rgb_e_r[V][H]=r
                rgb_e_g[V][H]=g
                rgb_e_b[V][H]=b
                V=V+1
            V=0
            H=H+1
        diff_r=0
        diff_g=0
        diff_b=0
        totaldiff_r=0
        totaldiff_g=0
        totaldiff_b=0
        for j in range(final_V):
            for k in range(final_H):
                if(rgb_o_r[j][k]!=rgb_e_r[j][k]):
                    diff_r=diff_r+1
                    totaldiff_r=totaldiff_r+(abs(rgb_o_r[j][k]-rgb_e_r[j][k])/(final_V*final_H*255))
                if(rgb_o_g[j][k]!=rgb_e_g[j][k]):
                    diff_g=diff_g+1
                    totaldiff_g=totaldiff_g+(abs(rgb_o_g[j][k]-rgb_e_g[j][k])/(final_V*final_H*255))
                if(rgb_o_b[j][k]!=rgb_e_b[j][k]):
                    diff_b=diff_b+1
                    totaldiff_b=totaldiff_b+(abs(rgb_o_b[j][k]-rgb_e_b[j][k])/(final_V*final_H*255))
        
        npcr_r=diff_r/(final_V*final_H)*100
        npcr_g=diff_g/(final_V*final_H)*100
        npcr_b=diff_b/(final_V*final_H)*100
        uaci_r=totaldiff_r*100
        uaci_g=totaldiff_g*100
        uaci_b=totaldiff_b*100

        
        w.writerow([no,origin[i],encode[i],"{:.4f}".format(npcr_r),"{:.4f}".format(npcr_g),"{:.4f}".format(npcr_b),"{:.4f}".format(uaci_r),
        "{:.4f}".format(uaci_g),"{:.4f}".format(uaci_b)])
        print('deal with the '+str(no)+" file")
        no=no+1
f2 = open('Output12.csv','w')
w = csv.writer(f2)
w.writerow(['No','ORI Images','ENC Image','NPCR(R)','NPCR(G)','NPCR(B)','UACI(R)','UACI(G)','UACI(B)'])
path = 'Origi_image'
path2 = 'Encry_image'
f_o = os.listdir('Origi_image')
f_e = os.listdir('Encry_image')
Encryption_Metrics(path,path2,w,f_o,f_e)
f2.close()