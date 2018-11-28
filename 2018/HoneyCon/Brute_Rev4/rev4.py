from itertools import product
from string import printable

v = [13, 60, 15, 72, 30, 87, 48] # Length 7

for p in product(printable, repeat=3):
    p = 'DcWx' + ''.join(p)
    v6 = 0
    v7 = 0
    for i in range(len(v)):
        v6 += ord(p[i])
        v7 += v[i] ^ ord(p[i])
    #print("v6: "+str(v6)+" - v7: "+str(v7)+" - Key: "+p)
    if (v6 == 666 and v7 == 569):
        print("Key found: "+p)
