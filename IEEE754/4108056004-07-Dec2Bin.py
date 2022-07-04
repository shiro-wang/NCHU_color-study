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

path = 'sideinfodeci.txt'
f = None
try:
    f = open(path, 'r')
    f2 = open('sideinfobina.txt','w')
    for line in f.readlines():
        i = float(line)
        test = floatToBinary32(i)
        j = "0"+(str)(test)
        f2.write(j+"\n")

except IOError:
    print('ERROR: can not found ' + path)
    if f:
        f.close()
finally:
    if f:
        f.close()
