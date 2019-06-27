# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen, quote
import requests
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '1iAUzSFoRNOC3Cc9wWiGGlmNuI5brif1' # 浏览器端密钥
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat, lng
if __name__ == '__main__':
    a,b=getlnglat('陕西省，西安市，西安科技大学临潼校区')
    print(a,b)

