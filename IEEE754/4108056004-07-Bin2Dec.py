import struct
import numpy as np
getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
 

def floatToBinary32(value):
    val = struct.unpack('L', struct.pack('f', value))[0]
    return getBin(val)
 

def binary32ToFloat(value):
    hx = hex(int(value, 2))   
    return struct.unpack("f", struct.pack("l", int(hx, 16)))[0]
 
# floats are represented by IEEE 754 floating-point format which are 
# 64 bits long (not 32 bits)
 
# float to binary

path = 'sideinfobina.txt'
f = None
try:
    f = open(path, 'r')
    f2 = open('sideinfodeci.txt','w')
    for line in f.readlines():
        # i = float(line)
        i = line[1:]
        # print(i)
        test = binary32ToFloat(i)
        f2.write((str)(test)+"\n")

except IOError:
    print('ERROR: can not found ' + path)
    if f:
        f.close()
finally:
    if f:
        f.close()
