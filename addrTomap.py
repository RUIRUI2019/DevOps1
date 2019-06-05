# -*- coding: utf-8 -*-
# import json
# from urllib.request import urlopen, quote
# import requests
# def getlnglat(address):
#     url = 'http://api.map.baidu.com/geocoder/v2/'
#     output = 'json'
#     ak = '1iAUzSFoRNOC3Cc9wWiGGlmNuI5brif1' # 浏览器端密钥
#     address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
#     uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
#     req = urlopen(uri)
#     res = req.read().decode()
#     temp = json.loads(res)
#     lat = temp['result']['location']['lat']
#     lng = temp['result']['location']['lng']
#     return lat, lng
# if __name__ == '__main__':
#     a,b=getlnglat('陕西省，西安市，西安科技大学临潼校区')
#     print(a,b)
# def calc( a, b, t):
#     # write code here
#     if t == 1:
#         sum0 = 0
#         for i in range(a):
#             sum0 += b
#         return sum0
#     if t == 0:
#         shang = 0
#         sum1 = 0
#         while sum1 != a:
#             sum1 += b
#             shang += 1
#         return shang
#     if t == -1:
#         cha = 0
#         res = min(a,b)
#         while res != max(a,b):
#             res += 1
#             cha += 1
#         if a>b:
#             return cha
#         else:
#             return -cha

def zipString( iniString):
    # write code here
    iniString = list(iniString)
    newString = []
    for i in iniString:
        iniString.pop(0)
        newString.append(iniString[0])
        count = 1
        while iniString[0] == newString[-1]:
            iniString.pop(0)
            count += 1
        newString.append(count)
    return ''.join(newString)
print(zipString('aabccd'))