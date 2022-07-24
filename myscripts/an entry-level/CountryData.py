# -*- coding: utf-8 -*-
"""

@author: 21
"""
import requests
import json
from bs4 import BeautifulSoup
import re
import pandas as pd

url='https://ncov.dxy.cn/ncovh5/view/pneumonia'
headers = { #safari
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding#apparent_encoding会从网页的内容中分析网页编码的方式
soup = BeautifulSoup(r.text, 'html.parser')#html解析和分析的工具
    
get_data1 = soup.find_all('script', attrs={'id': 'getListByCountryTypeService2true'})#soup.find函数进行查找匹配
get_data2 = get_data1[0].string
RE = re.compile('\[.*\]')  #.*？  表示匹配任意字符到下一个符合条件的字符
data_clear = re.findall(RE, get_data2)
data_clear[0]  # 这里有个列表，我们去除第0个
data_json = json.loads(data_clear[0])  # json.loads 将str类型的数据转换为dict类型
Number_of_Countrys = len(data_json)  

#提取数据到列表
id = []
continents = []
provinceName = []
countryFullName = []
currentConfirmedCount = []
confirmedCount = []
confirmedCountRank = []
suspectedCount = []
curedCount = []
deadCount = []
deadCountRank = []
deadRate = []
deadRateRank = []

for a in data_json:
    if 'id' in a:
        id.append(a['id'])
    else:
        id.append('没有')
    continents.append(a['continents'])
    provinceName.append(a['provinceName'])
    countryFullName.append(a['countryFullName'])
    currentConfirmedCount.append(a['currentConfirmedCount'])
    confirmedCount.append(a['confirmedCount'])
    if 'confirmedCountRank' in a:
        confirmedCountRank.append(a['confirmedCountRank'])
    else:
        confirmedCountRank.append('没有')
    suspectedCount.append(a['suspectedCount'])
    curedCount.append(a['curedCount'])
    deadCount.append(a['deadCount'])
    if 'deadCountRank' in a:
        deadCountRank.append(a['deadCountRank'])
    else:
        deadCountRank.append('没有')
    if 'deadRate' in a:
        deadRate.append(a['deadRate'])
    else:
        deadRate.append('没有')
    if 'deadRateRank' in a:
        deadRateRank.append(a['deadRateRank'])
    else:
        deadRateRank.append('没有')

#转换成pandas数组
df = {
    'id':pd.Series(id),
    '所在大洲':pd.Series(continents),#所在大洲
    '国家':pd.Series(provinceName),#国家
    'countryFullName':pd.Series(countryFullName),
    '当前确诊':pd.Series(currentConfirmedCount),#当前确诊
    '累计确诊':pd.Series(confirmedCount),#累计确诊
    '确诊排名':pd.Series(confirmedCountRank),#确诊排名
    '疑似病例':pd.Series(suspectedCount),#疑似病例
    '治愈人数':pd.Series(curedCount),#治愈人数
    '死亡人数':pd.Series(deadCount),#死亡人数
    '死亡人数排名':pd.Series(deadCountRank),#死亡人数排名
    '死亡率':pd.Series(deadRate),#死亡率
    '死亡率排名':pd.Series(deadRateRank)#死亡率排名
}
pds = pd.DataFrame(df)
pds.to_excel('../DataSets/CountryData.xlsx', index=False)
print("输出全球疫情数据成功！")

