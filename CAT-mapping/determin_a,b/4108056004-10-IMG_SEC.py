import random
import math
from decimal import *

f1 = open("input10.txt","r")
f2 = open("output10.txt",'w')
content = f1.readline()
contents = content.split(" ")
x0 = (float)(contents[0])
rx = float(contents[1])

content_2 = f1.readline()
contents_2 = content_2.split(" ")
y0 = (float)(contents_2[0])
ry = float(contents_2[1])

content_3 = f1.readline()
contents_3 = content_3.split(" ")
seed = int(contents_3[0])
N = int(contents_3[1])

content_4 = f1.readline()
L = float(content_4)

Rs = []
random.seed(seed)
for i in range(3):
    x = int(random.random()*N)
    Rs.append(x)
R1 = Rs[0]
R2 = Rs[1]
R3 = Rs[2]

for i in range(R1):
    xlo = rx * x0 * (1-x0)
    # print(x)
    x0 = xlo

for i in range(R2):
    ylo = ry * y0 * (1-y0)
    y0 = ylo

xand = math.ceil(x0/L)
yand = math.ceil(y0/L)

xans = R1 + xand
yans = R2 + yand

f2.write(content)
f2.write(content_2)
f2.write(content_3)
f2.write(content_4)
f2.writelines(str(R1)+" "+str(R2)+" "+str(R3)+'\n')
f2.write("%.21f "%x0)
f2.write("%.21f"%y0)
f2.write('\n')
f2.writelines(str(xans)+" "+str(yans))
    
f1.close()
f2.close()