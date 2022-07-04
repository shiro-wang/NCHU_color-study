from PIL import Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave
path = "ART-ENC-input08.txt"
f = None
try:
    f = open(path, 'r')
    f2 = open('ART-ENC-output08.txt','w')
    f3 = open('ART-DEC-input08.txt','w')
    for line in f.readlines():
        if(line != ""):
            data = line.split(" ")
            name = data[0]
            pos_neg = data[1]
            time = data[2]
            time = (int)(time)

            im = array(Image.open(name))
            im_p = im
            N = im.shape[0]
            # create x and y components of Arnold's cat mapping
            y,x = meshgrid(range(N),range(N))
            xmap = (2*x+y) % N
            ymap = (x+y) % N
            xdmap = (x-y) % N
            ydmap = (-x+2*y) % N
            p = 1
            im_p = im_p[xmap,ymap]
            con = array_equal(im_p,im)
            while(con == False):
                p = p+1
                im_p = im_p[xmap,ymap]
                con = array_equal(im_p,im)

            if(pos_neg == "+"):
                for i in range(time):
                    im = im[xmap,ymap]
            else:
                for i in range(time):
                    im = im[xdmap,ydmap]
            result = Image.fromarray(im)
            result.save("ART"+str(pos_neg)+str(time)+"_"+name)
            if(pos_neg == "+"):
                f2.write("ART"+str(pos_neg)+str(time)+"_"+name+" + "+str(time)+" "+str(p)+"\n")
                f3.write("ART"+str(pos_neg)+str(time)+"_"+name+" - "+str(time)+" "+str(p)+"\n")
            else:
                f2.write("ART"+str(pos_neg)+str(time)+"_"+name+" - "+str(time)+" "+str(p)+"\n")
                f3.write("ART"+str(pos_neg)+str(time)+"_"+name+" + "+str(time)+" "+str(p)+"\n")
        

except IOError:
    print('ERROR: can not found ' + path)
    if f:
        f.close()
finally:
    if f:
        f.close()

