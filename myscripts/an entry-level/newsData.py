# -*- coding: utf-8 -*-
"""

@author: 21
"""

import json
import pandas as pd

path='./json/news.json'
f=open(path,'r',encoding='utf-8')
newsdata=json.load(f)
newsdata_clear=newsdata['results']
n=len(newsdata)
#提取数据到列表
title=[]
summary=[]
infoSource=[]
sourceUrl=[]
province=[]

for a in newsdata_clear:
    title.append(a['title'])
    infoSource.append(a['infoSource'])
    sourceUrl.append(a['infoSource'])    
    summary.append(a['summary'])
    
df = {
      '新闻标题':pd.Series(title),
      '数据来源':pd.Series(infoSource),
      '来源链接':pd.Series(sourceUrl),      
      '新闻内容概述':pd.Series(summary),
      }
pds = pd.DataFrame(df)
pds.to_excel('../DataSets/newsData.xlsx', index=False)
print("新闻获取成功！")