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

from user_manage import app

@app.route('/try2')
def hello_world2():
    F1=request.args.get('user_date_start')
    F2=request.args.get('user_date_end')
    m1 = F1.strip().split("-")
    x1 = str(m1[1]) + "/" + str(m1[2]) + "/" + str(m1[0].strip("20"))
    m2 = F2.strip().split("-")
    x2 = str(m2[1]) + "/" + str(m2[2]) + "/" + str(m2[0].strip("20"))
    p = request.args.get("p", '')
    show_shouye_status = 0  # 显示首页状态

    if p == '':
        p = 1
    else:
        p = int(p)
        if p > 1:
            show_shouye_status = 1

    limit_start = (int(p) - 1) * 13  # 起始
    print(x1)
    print(x2)

    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    # sql = "SELECT * FROM history limit {0},13 WHERE equipment_id= '"+f+"'".format(xuhao=limit_start)
    sql = "SELECT * FROM  history  where ( DATE(time_bian) <='"+x2+"'and DATE(time_bian) >='"+x1+"')limit {0},13 ".format(limit_start)
    cursor.execute(sql)
    user_list = cursor.fetchall()

    # print("user_list-------------------------------", user_list)
    sql = "select count(xuhao) as total from history WHERE ( DATE(time_bian) <='"+x2+"'and DATE(time_bian) >='"+x1+"')"
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
        'user_date_start': F1,
        'user_date_end': F2,
        'show_shouye_status': show_shouye_status,
        'dic_list': dic

    }
    return render_template("history_show_time.html", datas=datas)

@app.route('/try1')
def hello_world1():
    F=request.args.get('equipment_id')
    f=str(F)
    print(f)
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
    # sql = "SELECT * FROM history limit {0},13 WHERE equipment_id= '"+f+"'".format(xuhao=limit_start)
    sql = "SELECT * FROM  history  where equipment_id= '"+f+"'limit {0},13 ".format(limit_start)
    cursor.execute(sql)
    user_list = cursor.fetchall()
    print(user_list)
    # print("user_list-------------------------------", user_list)
    sql = "select count(xuhao) as total from history WHERE equipment_id= '"+f+"'"
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
        'equipment_id': F,
        'show_shouye_status': show_shouye_status,
        'dic_list': dic

    }
    return render_template("history_show_id.html", datas=datas)

##计算设备的停机率
def tongji_tingji(xinghao):
    # print(xinghao)
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sq2 = "select state from history where equipment_id= '"+xinghao+"'"
    tingji1 = 0.0
    count = 0.0
    cursor.execute(sq2)
    u_rate = cursor.fetchall()
    db.close()
    for i in u_rate:
        if i[0] == str(0):
            tingji1 = tingji1 + 1
        count = count + 1
    rate = tingji1 / count
    return rate

@app.route('/zonghe1')
def zonghe1():
    ##(1)计算不同的型号有多少
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "select distinct equipment_id from history"
    cursor.execute(sql)
    u_distinct = cursor.fetchall()

    ###(2)得到当前处在第几页
    p = request.args.get("p", '')
    show_shouye_status = 0  # 显示首页状态

    if p == '':
        p = 1
    else:
        p = int(p)
        if p > 1:
            show_shouye_status = 1

    ##(3)计算现在的起始值
    limit_start = (int(p) - 1) * 13  # 起始
    user_list = []
    for i in range(limit_start, limit_start+13):
        if i < len(u_distinct):
            f = []
            rate = tongji_tingji(u_distinct[i][0])
            f.append(u_distinct[i][0])
            f.append(round(rate, 3))
            f.append(round(1 - rate, 3))
            user_list.append(f)
        else:
            break
    # print("count-------------------------------", count)
    total = int(math.ceil(len(u_distinct) / 13.0))  # 总页数
    dic = get_page(total, p)
    datas = {
        'user_list': user_list,
        'p': int(p),
        'total': total,
        'show_shouye_status': show_shouye_status,
        'dic_list': dic

    }
    return render_template("zonghefenxi1_all.html", datas=datas)

##历史信息显示界面##
@app.route('/history_show')
def history_show1():
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
    sql = "SELECT * FROM history limit {0},13".format(limit_start)
    cursor.execute(sql)
    user_list = cursor.fetchall()
    # print("user_list-------------------------------", user_list)
    sql = "select count(xuhao) as total from history"
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
    return render_template("history_show.html", datas=datas)



##
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

@app.route('/mainzzr')
def main2():
    return render_template('mainzzr_test.html')

# @app.route('/mainzzr2')
# def main2():
#     return render_template('mainzzr2_test.html')

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
    print(p)
    print("p")
    print(dic)
    print("dic")
    print(user_list)
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
    addr = request.args.get('addr')
    jing, wei = getlnglat(addr)
    jing_wei = str(jing) + '|' + str(wei)
    sql = "insert into equip_info(equipment_id,model,link_method,sale_date,linkman,addr,jing_wei,contacts,baoxiu,other) values" + \
          '(' + repr(request.args.get('equipment_id')) + ',' + \
          repr(request.args.get('model')) + ',' + \
          repr(request.args.get('link_method')) + ',' + \
          repr(request.args.get('sale_date')) + ',' + \
          repr(request.args.get('linkman')) + ',' + \
          repr(request.args.get('addr')) + ',' + \
          repr(jing_wei) + ',' + \
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

@app.route('/statistic')
def statistic_data():
    return render_template('statistic1.html')

@app.route('/history1')
def history1_data():
    return render_template('history1.html')

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
        tem['Sheding'] = i[3]
        tem['cycle_time'] = i[4]
        tem['quanshu'] = i[5]
        tem['program_number'] = i[6]
        tem['time_consuming'] = i[7]
        tem['Servo_alarm']=i[8]
        tem['Hard_limit_alarm'] = i[9]
        tem['Soft_limit_alarm'] = i[10]
        tem['Stop_alarm'] = i[11]
        tem['Equipment_condition_failure'] = i[12]
        tem['File_system_failure'] = i[13]
        tem['state'] = i[14]
        tem['time_bian'] = i[15]
        tem['time'] = str(time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
        jsondata.append(tem)
    print(jsondata)
    return json.dumps(jsondata)

@app.route('/machine_history',methods=['GET','POST'])
def machine_history_data():
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
        tem['Sheding'] = i[3]
        tem['cycle_time'] = i[4]
        tem['quanshu'] = i[5]
        tem['program_number'] = i[6]
        tem['time_consuming'] = i[7]
        tem['Servo_alarm']=i[8]
        tem['Hard_limit_alarm'] = i[9]
        tem['Soft_limit_alarm'] = i[10]
        tem['Stop_alarm'] = i[11]
        tem['Equipment_condition_failure'] = i[12]
        tem['File_system_failure'] = i[13]
        tem['time_bian'] = i[14]
        tem['time'] = str(time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
        jsondata.append(tem)
    print(jsondata)
    return json.dumps(jsondata)

@app.route('/showstatistic',methods=['GET','POST'])
def showstatistic_data():
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
        tem['test7']=i[8]
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
        tem['content'] = "型号：{0}<br/>出厂日期：{1}<br/>联系人：{2}<br/>电话：{3}".format(i[1],i[3],i[4],i[5])
        print(tem['content'])
        tem['point'] = i[6]
        tem['isopen'] = 0
        equip_list.append(tem)
    print(equip_list)
    return json.dumps(equip_list)

#删除设备信息
@app.route('/remove_equip/<string:equipment_id>',methods=['GET','POST'])
def remove_equip(equipment_id):
    print('删除设备')
    if equipment_id:
        db = pymysql.connect("localhost", "root", "123456", "opcdata")
        cursor = db.cursor()
        sql = "Delete FROM equip_info where equipment_id="+repr(equipment_id)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            do_thing = "用户：{yonghu}，删除设备操作执行成功".format(yonghu=session.get('username'))
            log_record(do_thing)
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
        db.close()
        print(3)
    return redirect('/equip_map/position')

#修改设备信息
@app.route('/equip_modify/<string:equipment_id>', methods=['GET', 'POST'])
def equip_modify(equipment_id):
    print('修改设备')
    if equipment_id:
        db = pymysql.connect("localhost", "root", "123456", "opcdata")
        cursor = db.cursor()
        sql = "select * FROM equip_info where equipment_id=" + repr(equipment_id)
        cursor.execute(sql)
        old_info = cursor.fetchall()
        print(old_info[0])
        print(type(old_info[0]))
        db.commit()
        db.close()
    return render_template('equip_modify.html', old_info=old_info[0])

#接受前端数据在数据库修改设备信息
@app.route('/equip_mod')
def equip_mod():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    addr = request.args.get('addr')
    jing, wei = getlnglat(addr)
    jing_wei = str(jing) + '|' + str(wei)

    sql = "update equip_info set sale_date="+repr(request.args.get('sale_date')) + ',' + \
          "link_method=" + repr(request.args.get('link_method')) + ',' + \
          "linkman="+repr(request.args.get('linkman')) + ',' +\
          "addr="+repr(request.args.get('addr')) + ',' + \
          "jing_wei=" + repr(jing_wei) + ',' + \
          "contacts=" + repr(request.args.get('contacts')) + ',' + \
          "baoxiu=" + repr(request.args.get('baoxiu')) + ',' + \
          "other=" + repr(request.args.get('other')) + \
          " where equipment_id=" + repr(request.args.get('equipment_id'))
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        do_thing = "用户：{yonghu}，进行了修改设备操作".format(yonghu=session.get('username'))
        log_record(do_thing=do_thing)
        return redirect('/equip_map/position')
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        flash('对不起添加失败le')
        return render_template('equip_modify.html')
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    app.run()