import csv
import math
import os
import numpy as np
from PIL import Image
import cv2

def Encryption_Metrics(path,w,f):
    no=1
    for file in f:
        name = str(file)
        im = Image.open(path+'/'+name)
        PixelArray = np.asarray(im)
        r_array=np.zeros(256)
        g_array=np.zeros(256)
        b_array=np.zeros(256)
        r_total=0
        g_total=0
        b_total=0
        H=0
        V=0
        
        tf=True
        for n, dim in enumerate(PixelArray):
            for num, row in enumerate(dim):
                r, g, b = row
                r_array[r]=r_array[r]+1
                g_array[g]=g_array[g]+1
                b_array[b]=b_array[b]+1
                if(tf):
                    V=V+1
            tf=False
            H=H+1
            
        total_pixel = V*H
        rv_total=0
        gv_total=0
        bv_total=0
        temp_rv=0
        temp_gv=0
        temp_bv=0
        temp_r=0
        temp_g=0
        temp_b=0
        pr_total=0
        pg_total=0
        pb_total=0
        for i in range(256):
            r_total = r_total+i*r_array[i]
            g_total = g_total+i*g_array[i]
            b_total = b_total+i*b_array[i]
            temp_rv = temp_rv + r_array[i]*r_array[i]
            temp_gv = temp_gv + g_array[i]*g_array[i]
            temp_bv = temp_bv + b_array[i]*b_array[i]
            temp_r = temp_r + r_array[i]
            temp_g = temp_g + g_array[i]
            temp_b = temp_b + b_array[i]
            pr = r_array[i]/total_pixel
            pg = g_array[i]/total_pixel
            pb = b_array[i]/total_pixel
            if(pr!=0):
                pr_total = pr_total+(pr*math.log(pr,2))
            if(pg!=0):
                pg_total = pg_total+(pg*math.log(pg,2))
            if(pb!=0):
                pb_total = pb_total+(pb*math.log(pb,2))
        
        r_median = r_total/total_pixel
        g_median = g_total/total_pixel
        b_median = b_total/total_pixel
        rv_total = temp_rv/256 - (temp_r/256)*(temp_r/256)
        gv_total = temp_gv/256 - (temp_g/256)*(temp_g/256)
        bv_total = temp_bv/256 - (temp_b/256)*(temp_b/256)
        pr_total=0-pr_total
        pg_total=0-pg_total
        pb_total=0-pb_total
        w.writerow([no,name,"{:.2f}".format(r_median),"{:.2f}".format(g_median),"{:.2f}".format(b_median),"{:.2f}".format(round(rv_total, 2)),
        "{:.2f}".format(round(gv_total, 2)),"{:.2f}".format(round(bv_total, 2)),"{:.6f}".format(pr_total),"{:.6f}".format(pg_total),"{:.6f}".format(pb_total)])
        no=no+1
f2 = open('Output11.csv','w')
w = csv.writer(f2)
w.writerow(['No','Images','MIR','MIG','MIB','VHR','VHG','VHB','SER','SEG','SEB'])
path = 'Origi_image'
f_o = os.listdir('Origi_image')
Encryption_Metrics(path,w,f_o)
f2.close()

f2 = open('Output11_en.csv','w')
w = csv.writer(f2)
w.writerow(['No','Images','MIR','MIG','MIB','VHR','VHG','VHB','SER','SEG','SEB'])
path = 'Encry_image'
f_e = os.listdir('Encry_image')
Encryption_Metrics(path,w,f_e)
f2.close()

f2 = open('Output11_de.csv','w')
w = csv.writer(f2)
w.writerow(['No','Images','MIR','MIG','MIB','VHR','VHG','VHB','SER','SEG','SEB'])
path = 'Decry_image'
f_d = os.listdir('Decry_image')
Encryption_Metrics(path,w,f_d)
f2.close()
    
