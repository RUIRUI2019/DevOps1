from flask import Flask
from flask import render_template,request,flash,redirect,session
import json
import pymysql
import time
import traceback

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

from user_manage import app

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
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM equip_info"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    return render_template('equip_position.html',u=u)

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

@app.route('/equip_problem/threshold')
def threshold():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM problem_info"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    print(u)
    return render_template('threshold.html',u=u)

if __name__ == '__main__':
    app.run(port=8888,debug=True)
