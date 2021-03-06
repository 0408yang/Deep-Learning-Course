# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:29:32 2020

@author: yjh
"""

import numpy as np
x0=np.ones((10),dtype=np.float64)
x1=np.array([64.30,99.60,145.45,63.75,135.46,92.85,86.97,144.76,59.30,116.03],dtype=np.float64)
x2=np.array([2.,3.,4.,2.,3.,4.,2.,4.,1.,3.],dtype=np.float64)
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
X=np.stack((x0,x1,x2),axis=1 )
Y=y.reshape(10,1)

X=np.mat(X)
Y=np.mat(Y)
W=((X.T*X)**(-1))*(X.T*Y)
print("X:\n",X)
print("Y:\n",Y)
print("W:\n",W)
print("W的形状是:{}".format(W.shape))