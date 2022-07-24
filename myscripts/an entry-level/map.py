# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:27:33 2022

@author: 21
"""
#工具包
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts
#作图数据
data = pd.read_excel('../DataSets/CountryData.xlsx',index_col=0)

#作全球疫情地图
c=(
   Map(init_opts=opts.InitOpts(width="1400px",height='600px'))#图表大小
   #添加数据系列名称，数据（list格式），地图名称，不显示小红点
   .add("",[list(z) for z in zip(data['countryFullName'],data['累计确诊'])],"world",is_map_symbol_show=False,name_map=data['国家'])
   .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 标签不显示(国家名称不显示)
   .set_global_opts(
        title_opts=opts.TitleOpts(title="2022全球疫情",subtitle='单位: 人'),   # 主标题与副标题名称
        visualmap_opts=opts.VisualMapOpts(is_show=True,
                                          split_number=7,
                                          is_piecewise=True,  # 是否为分段型
                                          pos_top='center',
                                          pieces=[
                                                {'min': 50000000, 'color': '#7f1818'},  #不指定 max
                                                {'min': 10000000,'max': 49999999,'color':'#990012'},
                                                {'min': 1000000, 'max': 9999999,'color':'#C11B17'},
                                                {'min': 500000, 'max': 999999,'color':'#C04000'},
                                                {'min': 100000, 'max': 499999,'color':'#C34A2C'},
                                                {'min': 10000, 'max': 99999,'color':'#E18B6B'},
                                                {'min': 0, 'max': 9999,'color':'#FAEBD7'}],                                              
                                            ),
    )
   )
c.render("html/2022全球疫情地图.html") #生成html文件


#中国疫情地图
data2=pd.read_excel('../DataSets/PronvicesData.xlsx',index_col=None)
list_data = zip(data2['省份'], data2['当前确诊'])
d=(
    Map()#图表大小s
   #添加数据系列名称，数据（list格式），地图名称，不显示小红点
   .add("",[list(z) for z in list_data],"china",is_map_symbol_show=False)
   .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 标签不显示(国家名称不显示)
   .set_global_opts(
        title_opts=opts.TitleOpts(title="2022中国疫情分布图",subtitle='单位: 人'),   # 主标题与副标题名称
        visualmap_opts=opts.VisualMapOpts(is_show=True,
                                          split_number=6,
                                          is_piecewise=True,  # 是否为分段型
                                          pos_top='center',
                                          pieces=[
                                                {'min': 10000, 'color': '#7f1818'},  #不指定 max
                                                {'min': 1000, 'max': 10000,'color':'#C11B17'},
                                                {'min': 500, 'max': 999,'color':'#C04000'},
                                                {'min': 100, 'max': 499,'color':'#C34A2C'},
                                                {'min': 10, 'max': 99,'color':'#E18B6B'},
                                                {'min': 0, 'max': 9,'color':'#FAEBD7'}],                                              
                                            ),
    )
   )
d.render("html/2022-5-2中国疫情地图.html")
