# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:53:42 2022

@author: 21
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
def re_encode(path):#定义编码转换
    with open(path,'r',encoding='GB2312',errors='ignore') as file:
        lines =file.readlines()#读取所有行并返回列表 
    with open(path,'w',encoding='utf-8') as file:
        file.write(''.join(lines))#用于向文件中写入指定
        
re_encode('nCov_10k_test.csv') #测试集转换编码
re_encode('nCoV_100k_train.labled.csv')#训练集转换编码
"""

data =pd.read_csv('nCoV_100k_train.labled.csv',
                  encoding='utf-8',
                  engine='python')
data.head()

#数据预处理

#将异常值去除
data = data[data['情感倾向'].isin(['-1','0','1'])]
#将label转化为整型
data['情感倾向'] = data['情感倾向'].astype(np.int32)

#查看训练集各变量的类型数量等信息，同时查看标签数据
data.info(memory_usage='deep')#得到较准确的数据
print(data['情感倾向'].value_counts())

x=np.arange(3)
y=data['情感倾向'].value_counts()/data['情感倾向'].count()
x_label=['neutral','positive','negative']
plt.xticks(x,x_label)
plt.bar(x,y)
