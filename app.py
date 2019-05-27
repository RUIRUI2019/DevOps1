from flask import Flask
from flask import render_template,request,flash,redirect,session
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

from user_manage import app

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

@app.route('/index')
def hello_world():
    return render_template('index.html')
@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/equip_map')
def equip_map():
    return render_template('equip_map.html')

@app.route('/equip_map/baidu')
def baidu():
    return render_template('map.html')

@app.route('/equip_map/position')
def position():
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
    sql = "SELECT * FROM equip_info limit {0},13".format(limit_start)
    cursor.execute(sql)
    user_list = cursor.fetchall()
    # print("user_list-------------------------------", user_list)
    sql = "select count(equipment_id) as total from equip_info"
    cursor.execute(sql)
    count = cursor.fetchone()  # 总记录
    db.close()
    # print("count-------------------------------", count)
    total = int(math.ceil(count[0] / 13.0))  # 总页数
    dic = get_page(total, p)
    datas = {
        'user_list': user_list,
        'p': int(p),
        'total': total,
        'show_shouye_status': show_shouye_status,
        'dic_list': dic

    }
    return render_template("equip_position.html", datas=datas)

@app.route('/equip_tianjia')
def equip_tianjia():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "insert into equip_info(equipment_id,model,sale_date,linkman,addr,contacts,baoxiu,other) values" + \
          '(' + repr(request.args.get('equipment_id')) + ',' + \
          repr(request.args.get('model')) + ',' + \
          repr(request.args.get('sale_date')) + ',' + \
          repr(request.args.get('linkman')) + ',' + \
          repr(request.args.get('addr')) + ',' + \
          repr(request.args.get('contacts')) + ',' + \
          repr(request.args.get('baoxiu')) + ',' + \
          repr(request.args.get('other')) + ')'
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        do_thing = "用户：{yonghu}，进行了添加设备操作".format(yonghu=session.get('username'))
        log_record(do_thing=do_thing)
        return redirect('/equip_map/position')
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        flash('对不起添加失败le')
        return render_template('position_add.html')
    # 关闭数据库连接
    db.close()

@app.route('/equip_map/position/position_add')
def position_add():
    return render_template('position_add.html')

@app.route('/equip_data')
def equip_data():
    return render_template('equip_data.html')

@app.route('/machin',methods=['GET','POST'])
def machine_data():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='opcdata', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM equip_data"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    jsondata = []
    for i in u:
        tem = {}
        tem['equipment_id'] = i[0]
        tem['maxis_speed'] = i[1]
        tem['current_yield'] = i[2]
        tem['dan_lian'] = i[3]
        tem['cycle_time'] = i[4]
        tem['material_num'] = i[5]
        tem['speed'] = i[6]
        tem['quanshu'] = i[7]
        tem['time'] = str(time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
        jsondata.append(tem)
    print(jsondata)
    return json.dumps(jsondata)

@app.route('/equip_problem/threshold0')
def threshold0():
    print('ceshi')
    return render_template('threshold.html')

@app.route('/threshold1',methods=['GET','POST'])
def threshold1():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM problem_info"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    data_list = []
    for i in u:
        tem = {}
        tem['equipment_id'] = i[0]
        tem['fault_point'] = i[1]
        tem['fault_tag'] = i[2]
        tem['current_value'] = i[3]
        tem['limit_value'] = i[4]
        tem['fault_time'] = i[5]
        data_list.append(tem)
    print(data_list)
    return json.dumps(data_list)

@app.route('/bar_data',methods=['GET','POST'])
def bar_data():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM fault_rate"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    data_list = []
    for i in u:
        tem = {}
        tem['equipment_id'] = i[0]
        tem['rate'] = i[1]
        data_list.append(tem)
    print(data_list)
    return json.dumps(data_list)

@app.route('/addrTojson',methods=['GET','POST'])
def addrTojson():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM equip_info"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    equip_list = []
    for i in u:
        tem = {}
        tem['title'] = i[0]
        tem['content'] = "型号：{0}<br/>出厂日期：{1}<br/>联系人：{2}<br/>电话：{3}".format(i[1],i[2],i[3],i[5])
        print(tem['content'])
        jing,wei = getlnglat(i[4])
        tem['point'] = str(jing)+'|'+str(wei)
        tem['isopen'] = 0
        equip_list.append(tem)
    print(equip_list)
    return json.dumps(equip_list)

if __name__ == '__main__':
    app.run(port=8888,debug=True)
