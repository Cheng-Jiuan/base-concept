#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:11:51 2022

@author: candy
"""

# ANOVA 檢定
# 單向F檢驗（需要修改）
# 根據兩個或更多個組的平均相似度來判斷是否相似
df_anova = pd.read_csv('PlantGrowth.csv') #讀取資料檔
df_anova = df_anova[['grade','group']] #有3種不同的類別及其成績，需要檢查所有3組是否相似
grps = pd.unique(df_anova.group.values)
d_data = {grp:df_anova['grade'][df_anova.group == grp] for grp in grps}
 F, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2']) 
 f_value,p_value = st.f_oneway(alist, blist, clist)
if p<0.05: 
   print("拒絕虛無假設")
else:  
  print("接受虛無假設")
  
  
# 多因子變異數檢定
import statsmodels.api as sm
from statsmodels.formula.api import sta
df = pd.read_csv('grade.csv')
model = sta('成績 ~ C(家庭教育) + C(地區) + C(家庭教育):C(地區)', data=df).fit()
Results = sm.stats.anova_lm(model)
