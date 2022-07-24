# -*- coding: utf-8 -*-
# By: Eastmount CSDN xiuzhang

import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line


url="../DataSets/historydata.xlsx"
#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
#line
data = pd.read_excel(url,index_col=None)
date_list = list(data['日期'])
date_list = list(map(lambda x:str(x),date_list))
confirm_list = list(data['累计确诊'])
current_list=list(data['当前确诊'])
dead_list = list(data['死亡人数'])
heal_list = list(data['治愈人数'])

#line2
add_list =list(data['新增确诊'])
suspect_list=list(data['疑似病例新增'])
input_list=list(data['外来输入新增'])
print(len(date_list))    

#-------------------------------------------------------------------------------------
# 第二步：绘制折线图
#-------------------------------------------------------------------------------------
line = (
        Line()
        .set_global_opts(
        title_opts=opts.TitleOpts(title="全国累计确诊数据趋势",subtitle='单位: 人'),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(date_list)
    .add_yaxis('累计确诊数据', confirm_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis('死亡数据', dead_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis('治愈数据', heal_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis('现存确诊', current_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    )
line.render("html/COVID历史数据走势.html")

a =(
        Line()
        .set_global_opts(
        title_opts=opts.TitleOpts(title="全国新增确诊/境外输入数据趋势",subtitle='单位: 人'),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(date_list)
    .add_yaxis('新增确诊', add_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis('新增疑似', suspect_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    )
a.render("html/新增.html")

b =(
        Line()
        .set_global_opts(
        title_opts=opts.TitleOpts(title="全国境外输入数据趋势",subtitle='单位: 人'),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(date_list)
    .add_yaxis('外来输入', input_list, is_smooth=True,label_opts=opts.LabelOpts(is_show=False))
    )
b.render("html/境外输入新增.html")
    
