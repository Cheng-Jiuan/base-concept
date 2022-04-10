#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:59:54 2022

@author: candy
"""
#Z檢定
#前後測
import pandas as pd
from scipy import stats
df = pd.read_csv("test.csv")
df[['test_before','test_after']].describe()
ttest,pval = stats.ttest_rel(df['test_before'], df['test_after'])
print(pval)
if pval<0.05:
    print("拒絕虛無假設")
else:
    print("接受虛無假設")
    
#單一z檢定
import pandas as pd
from scipy import statsfrom statsmodels.stats 
 import weight stats as stestsztest ,pval = stests.ztest(df['test_before'], x2=None, value=88) #88個單樣本Z檢驗
print(float(pval))
if pval<0.05:
    print("拒絕虛無假設")
else:   
 print("接受虛無假設")

#成對樣本z檢定
ztest ,pval1 = stests.ztest(df['test_before'],
x2=df['test_after'],
value=0,alternative='two-sided') #平均值為0,雙尾
print(float(pval1))
if pval<0.05:
    print("拒絕虛無假設")
    else:    
        print("接受虛無假設")