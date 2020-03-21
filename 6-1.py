# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:40:59 2020

@author: zhaojf
"""

import matplotlib.pyplot as pl
import numpy as np

pl.rcParams['font.sans-serif']='SimHei'
pl.rcParams['axes.unicode_minus']=False

x=np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
y=np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
pl.scatter(x,y,color="red")
pl.title("商品房销售记录",color="blue",fontsize=16)
pl.xlim(30,200)
pl.ylim(30,200)
pl.xlabel('面积（平方米）',fontsize=14)
pl.ylabel('价格（万元）',fontsize=14)
pl.show()