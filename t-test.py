#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:47:41 2022

@author: candy
"""

# =========== 單一樣本t檢定 =====================
from scipy.stats import ttest_1samp
import numpy as np
task = np.genfromtxt("task.csv") #讀取資料夾
print(task)
tasks_mean = np.mean(tasks) #算平均數
print(tasks_mean)
    
# 單一樣本t檢定
tset, pval = ttest_1samp(task, 5) #task是否為5
print("p-values",pval)
    
if pval < 0.05:    # alpha value is 0.05 or 5%   
    print("拒絕虛無假設")
else: 
    print("接受虛無假設")      

#峰度、偏態與常態分配檢定
# 峰度 偏態
from scipy.stats import skew, kurtosis
v = np.random.normal(size=50) #size=50可以輸入自己的檔案

print(skew(v))
print(kurtosis(v))

# 是否為常態分佈
from scipy.stats import normaltest
v = np.random.normal(size=50) #size=50可以輸入自己的檔案
print(normaltest(v))



# =========== 成對樣本t檢定 =====================
from scipy.stats import ttest_ind
import numpy as np

# 讀取資料夾
tesk1 = np.genfromtxt("tesk1.csv",  delimiter=",")
tesk2 = np.genfromtxt("tesk2.csv",  delimiter=",")
print(tesk1)
print(tesk2)

#算平均值
tesk1_mean = np.mean(tesk1)
week2_mean = np.mean(tesk2)
print("tesk1 mean value:",tesk1_mean)
print("tesk2 mean value:",tesk2_mean)

#算標準差
tesk1_std = np.std(tesk1)
tesk2_std = np.std(week2)
print("tesk1 std value:",tesk1_std)
print("tesk2 std value:",tesk2_std)

#進行檢定
ttest,pval = ttest_ind(tesk1,tesk2)
print("p-value",pval)
if pval <0.05:  
    print("拒絕虛無假設")
else:  
    print("接受虛無假設"）
                 