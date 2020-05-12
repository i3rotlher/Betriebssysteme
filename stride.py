#! /usr/bin/env python
# coding=utf-8

import sys
from optparse import OptionParser
import random
import array
import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
stride = 10
strideinc = 10
pro0 = 0
pro1 = 0
for i in range(1000):
    pro0 = stride
    print pro0
    stride += strideinc
    pro1 = stride
    print pro1
    data.append(float(pro0)/pro1)
    stride += strideinc

print data
#plot with matplotlib
x = [1, 10, 100]
plt.ylim(0.5, 1)
plt.xlim(1,100)
plt.xticks(x)
plt.plot(data)
plt.ylabel("Unfairness")
plt.xlabel("Job Length")
plt.show()