#Problem        : Giga Ball++
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.1
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

l = int(raw_input())
m = int(raw_input())
n = int(raw_input())
a = []
b = []
c = []
for i in range(l):
    a.append(int(raw_input())
for i in range(m):
    b.append(int(raw_input())
for i in range(n):
    c.append(int(raw_input())

mm = {}
maxs = -1
for x in range(l):
    for y in range(m):
        for z in range(n):
            s = a[x]+b[y]+c[z]
            if s in mm:
                mm[s] += 1
            else:
                mm[s] = 1
            if (maxs == -1) or (mm[maxs] < mm[s]):
                maxs = s
    
print maxs
                

