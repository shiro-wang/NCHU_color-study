from PIL import Image
from numpy import *
#from scipy.misc import lena,imsave
#from scipy.misc import imsave
path = "ART-DEC-input08.txt"
f = None
try:
    f = open(path, 'r')
    f2 = open('ART-DEC-output08.txt','w')
    for line in f.readlines():
        if(line != ""):
            data = line.split(" ")
            name = data[0]
            pos_neg = data[1]
            time = data[2]
            time = (int)(time)
            
            im = array(Image.open(name))
            N = im.shape[0]
            # create x and y components of Arnold's cat mapping
            y,x = meshgrid(range(N),range(N))
            xmap = (2*x+y) % N
            ymap = (x+y) % N
            xdmap = (x-y) % N
            ydmap = (-x+2*y) % N

            if(pos_neg == "+"):
                for i in range(time):
                    im = im[xmap,ymap]
            else:
                for i in range(time):                    
                    im = im[xdmap,ydmap]
            result = Image.fromarray(im)
            result.save("AFTER_All_"+name)
            names = name.split("_")
            final_name = names[1]
            f2.write(final_name+'\n')

except IOError:
    print('ERROR: can not found ' + path)
    if f:
        f.close()
finally:
    if f:
        f.close()

