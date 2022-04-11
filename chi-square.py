#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 22:51:44 2022

@author: candy
"""

# 卡方檢定
import numpy as np 
import scipy.stats
obs = np.array([[32,43,16,9], [55,65,64,16]]) #輸入資料的值
scipy.stats.chi2_contingency(obs, correction = False)
# 統計值
# p值（卡方是否<.05) 
# 自由度