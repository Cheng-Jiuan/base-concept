#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:47:41 2022

@author: candy
"""

# t檢定
from scipy import stats 
import numpy as np

#輸入資料集
Test1 = np.array([1,2,3,4,5]) #樣本<30

#單一樣本t檢定
a=stats.ttest_1samp(Test1, popmean=3) 

if a[1]<0.05:print('testmean<3')
else:
    print('testmean=3')
    
#H0:數值平均數等於3
#H1:數值平均數不等於3






