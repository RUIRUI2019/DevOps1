from flask import Flask
from flask import render_template,request,flash,redirect,session,url_for
import json
import pymysql
import time
import traceback
from user_manage import log_record,get_page
import math
from urllib.request import urlopen, quote
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/zonghe1')
def zonghe1():
    p = request.args.get("p", '')
    show_shouye_status = 0  # 显示首页状态

    if p == '':
        p = 1
    else:
        p = int(p)
        if p > 1:
            show_shouye_status = 1

    limit_start = (int(p) - 1) * 13  # 起始

    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "select Stop_alarm from history where equipment_id= 'GRM231'"
    tingji1 = 0.0
    count = 0.0
    cursor.execute(sql)
    u = cursor.fetchall()
    print(u)
    db.close()
    for i in u:
        print(i[0])
        if i[0] == "False":
            tingji1 = tingji1 + 1
        count = count + 1

    rate = tingji1 / count
    user_list=[]
    f=[]
    f.append("GRM231")
    f.append(rate)
    f.append(1-rate)
    user_list.append(f)
    # print("count-------------------------------", count)
    total = int(math.ceil(1 / 13.0))  # 总页数
    dic = get_page(total, p)
    datas = {
        'user_list': user_list,
        'p': int(p),
        'total': total,
        'show_shouye_status': show_shouye_status,
        'dic_list': dic

    }
    return render_template("zonghefenxi1_all.html", datas=datas)
