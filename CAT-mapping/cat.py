import cv2
import numpy as np

def transform(img, num, name):

    rows, cols, ch = img.shape
    if (rows == cols):
        n = rows
        img2 = np.zeros([rows, cols, ch])

        for x in range(0, rows):
            for y in range(0, cols):

                img2[x][y] = img[(x+y)%n][(x+2*y)%n]

        cv2.imwrite(name + "_" +str(num) + ".bmp", img2)
        return img2

    else:
        print("The image is not square.")
def detransform(img, num, name):

    rows, cols, ch = img.shape
    if (rows == cols):
        n = rows
        img2 = np.zeros([rows, cols, ch])

        for x in range(0, rows):
            for y in range(0, cols):

                img2[x][y] = img[(2*x-y)%n][(-x+y)%n]

        cv2.imwrite(name + "_" + str(num) + ".bmp", img2)
        return img2

    else:
        print("The image is not square.")
def findperiod(img, imgtemp):

    rows, cols, ch = img.shape
    if (rows == cols):
        p=1
        n = rows
        
        img2 = np.zeros([rows, cols, ch])
        for x in range(0, rows):
            for y in range(0, cols):
                img2[x][y] = img[(2*x-y)%n][(-x+y)%n]
        tf = True
        while(tf):
            tf = False
            p = p+1
            img = img2
            for x in range(0, rows):
                for y in range(0, cols):
                    img2[x][y] = img[(2*x-y)%n][(-x+y)%n]
            for x in range(0, rows):
                for y in range(0, cols):
                    if(img2[x][y] != imgtemp[x][y]):
                        tf = True
                        break;
                if(tf):
                    break;
        return p

    else:
        print("The image is not square.")

img = cv2.imread('BeaverDam-800.bmp')
img = transform(img, 1, "BeaverDam-800")
img = cv2.imread('BeaverDam-800_1.bmp')
img = detransform(img, -1, "BeaverDam-800")
img = cv2.imread('BeaverDam-800.bmp')
p = findperiod(img, img)
print(p)
