#coding=utf-8
import requests

try:
    cityname = raw_input('你想查看那个城市的天气?\n')
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityname
    r = requests.get(url)
    data = r.json()
    result = data['data']

    print '当前温度',result['wendu'],'度'
except:
    print '查询失败'
