import random
import csv
import math

f1 = open("input09.txt","r")
f2 = open("output09.csv",'w')
content = f1.readline()
contents = content.split(" ")
x0 = (float)(contents[0])
r = float(contents[1])
N = int(contents[2])
seed = int(contents[3])
if(x0<1 and x0>0 and r<=4 and r>3.569945):
    logistic = []
    log_all = 0
    for i in range(N):
        x = r * x0 * (1-x0)
        logistic.append(x)
        # print(x)
        x0 = x
        log_all = log_all + x
    log_mean = log_all/N
    l_pow = 0
    for i in logistic:
        l = pow(i-log_mean,2)
        l_pow = l_pow+l
    l_pow = l_pow/N
    l_std = math.sqrt(l_pow)

    ran = []    
    random.seed(seed)
    ran_all = 0
    for i in range(N):
        x = random.random()
        ran.append(x)
        # print(x)
        ran_all = ran_all + x
    ran_mean = ran_all/N
    r_pow = 0
    for i in ran:
        r = pow(i-ran_mean,2)
        r_pow = r_pow+r
    r_pow = r_pow/N
    r_std = math.sqrt(r_pow)
    
    w = csv.writer(f2)
    w.writerow(['x0','r','N','seed'])
    for i in range(N):
        w.writerow([i+1,"{:.6f}".format(logistic[i]),"{:.6f}".format(ran[i])])
    w.writerow(['mean',"{:.6f}".format(log_mean),"{:.6f}".format(ran_mean)])
    w.writerow(['std',"{:.6f}".format(l_std),"{:.6f}".format(r_std)])
f1.close()
f2.close()