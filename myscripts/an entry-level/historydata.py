# -*- coding: utf-8 -*-
"""
Created on Mon May  2 22:00:21 2022

@author: 21
"""

import requests #爬取网页
import json #爬取数据
import pandas as pd
url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=329822670771'
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'}
response = requests.get(url , headers = headers)
#print(response.status_code) #200表示访问成功
#print(response.json()) # 打印内容

jsondata = response.json()['data']['chinaDayList']
n=len(jsondata)

#提取数据到列表
date=[]#日期
confirm=[]#累计确诊
deadCount=[]#死亡人数
curedCount=[]#治愈人数
currentConfirm=[]#现存确诊
suspectIncur=[]#新增疑似病例
inputCount=[] #外来输入
confirmIncur=[]#新增确诊
for i in range(n):
    history_data=jsondata[i]
    date.append(history_data['date'])
    confirm.append(history_data['total']['confirm'])
    deadCount.append(history_data['total']['dead'])
    curedCount.append(history_data['total']['heal'])
    currentConfirm.append(history_data['total']['storeConfirm'])
    suspectIncur.append(history_data['today']['suspect'])
    inputCount.append(history_data['today']['input'])
    confirmIncur.append(history_data['today']['confirm'])

df = {
    '日期':pd.Series(date),
    '累计确诊':pd.Series(confirm),
    '当前确诊':pd.Series(currentConfirm),
    '治愈人数':pd.Series(curedCount),#治愈人数
    '死亡人数':pd.Series(deadCount),#死亡人数
    '新增确诊':pd.Series(confirmIncur),#新增确诊
    '疑似病例新增':pd.Series(suspectIncur),#疑似病例新增
    '外来输入新增':pd.Series(inputCount)#疑似病例新增
}
pds = pd.DataFrame(df)
pds.to_excel('../DataSets/historydata2.xlsx', index=False)
print("输出历史数据成功")