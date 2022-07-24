# -*- coding: utf-8 -*-
"""

@author: 21
"""
import requests
import json
from bs4 import BeautifulSoup
import re
import pandas as pd

#我们要获取每一个国家地区和中国每一个省市疫情数据对应的列表。通过python中的requests库获取页面
#def getlist(url): 也可以写一个API
url='https://ncov.dxy.cn/ncovh5/view/pneumonia'
headers = { #safari
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding#apparent_encoding会从网页的内容中分析网页编码的方式
soup = BeautifulSoup(r.text, 'html.parser')#html解析和分析的工具
    
get_data1 = soup.find_all('script', attrs={'id': 'getAreaStat'})#soup.find函数进行查找匹配
get_data2 = get_data1[0].string
RE = re.compile('\[.*\]')  #.*？  表示匹配任意字符到下一个符合条件的字符
data_clear = re.findall(RE, get_data2)
data_clear[0]  # 这里有个列表，我们去除第0个
data_json = json.loads(data_clear[0])  # json.loads 将str类型的数据转换为dict类型
Number_of_China_provinces = len(data_json)  # 查看有几个省市，用于遍历。由常识可知，中华人民共和国有34个省级行政区域，包括23个省，5个自治区，4个直辖市，2个特别行政区。

#提取数据到列表
cities=[]
provinceName = []
currentConfirmedCount = []
confirmedCount = []
suspectedCount = []
curedCount = []
deadCount = []

for a in data_json:
    cities.append(a['cities'])#省份下的城市
    provinceName.append(a['provinceName'])
    currentConfirmedCount.append(a['currentConfirmedCount'])
    confirmedCount.append(a['confirmedCount'])
    suspectedCount.append(a['suspectedCount'])
    curedCount.append(a['curedCount'])
    deadCount.append(a['deadCount'])

#转换成pandas数组
df = {
    '省份':pd.Series(provinceName),#省份
    '当前确诊':pd.Series(currentConfirmedCount),#当前确诊
    '累计确诊':pd.Series(confirmedCount),#累计确诊
    '疑似病例':pd.Series(suspectedCount),#疑似病例
    '治愈人数':pd.Series(curedCount),#治愈人数
    '死亡人数':pd.Series(deadCount),#死亡人数
}
pds = pd.DataFrame(df)
pds.to_excel('../DataSets/PronvicesData.xlsx', index=False)
print("输出中国疫情数据成功！")