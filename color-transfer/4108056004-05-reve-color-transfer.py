from color_transfer import color_transfer
import numpy as np
import argparse
import cv2

# python 4108056004-05-reve-color-transfer.py --source photo\sou.png --target photo\tar.png

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True,
	help = "Path to the source image")
ap.add_argument("-t", "--target", required = True,
	help = "Path to the target image")
ap.add_argument("-c", "--clip", type = str2bool, default = 't',
	help = "Should np.clip scale L*a*b* values before final conversion to BGR? "
		   "Approptiate min-max scaling used if False.")
ap.add_argument("-p", "--preservePaper", type = str2bool, default = 't',
	help = "Should color transfer strictly follow methodology layed out in original paper?")
ap.add_argument("-o", "--output", help = "Path to the output image (optional)")
args = vars(ap.parse_args())

# load the images
source = cv2.imread(args["source"])
target = cv2.imread(args["target"])

# transfer the color distribution from the source image
# to the target image
transfer = color_transfer(target, source, clip=args["clip"], preserve_paper=args["preservePaper"])

# check to see if the output image should be saved
if args["output"] is not None:
	cv2.imwrite(args["output"], transfer)

# show the images and wait for a key press

(l, a, b) = cv2.split(transfer)
result=[]
l = np.float32(l)
a = np.float32(a)
b = np.float32(b)

path = 'sideinfodeci.txt'
f = None
try:
    f = open(path, 'r')
    for line in f.readlines():
        result.append(line)
    
    l -= np.float32(result[6])
    a -= np.float32(result[7])
    b -= np.float32(result[8])

    l = (np.float32(result[3]) / np.float32(result[9]))*l
    a = (np.float32(result[4]) / np.float32(result[10]))*a
    b = (np.float32(result[5]) / np.float32(result[11]))*b

    l += np.float32(result[0])
    a += np.float32(result[1])
    b += np.float32(result[2])

    reverse_image = cv2.merge([l,a,b])
    cv2.imwrite('C:\\Users\\user\\Desktop\\Python\\color\\yrcsou.png', reverse_image)
except IOError:
    print('ERROR: can not found ' + path)
    if f:
        f.close()
finally:
    if f:
        f.close()

    


cv2.imwrite('C:\\Users\\user\\Desktop\\Python\\color\\ult.png', transfer)

cv2.waitKey(0)