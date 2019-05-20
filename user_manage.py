from flask import Flask
from flask import render_template,request,flash,session,redirect,url_for
import pymysql
import traceback
from io import BytesIO
import validate_code
import time
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route('/code')
def get_code():
    # 把strs发给前端,或者在后台使用session保存
    code_img, strs = validate_code.create_validate_code()
    buf = BytesIO()
    code_img.save(buf, 'jpeg')

    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    session['img'] = strs.upper()
    print(session['img'])
    print(response)
    return response

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        print('post====================================')
        print(request.form.get('yanzhengma'))
        if session.get('img') == (request.form.get('yanzhengma')).upper():
            db = pymysql.connect("localhost", "root", "123456", "opcdata")
            cursor = db.cursor()
            sql = "select * from user where username=" + repr(request.form.get('username')) + " and password=" + repr(
                request.form.get('password'))
            print(sql)
            try:
                # 执行sql语句
                cursor.execute(sql)
                results = cursor.fetchall()
                print(request.form.get('password'))
                if len(results) == 1:
                    # flash('登录成功')
                    username = request.form.get('username')
                    session['username'] = username
                    do_thing = "用户：{yonghu}，登录系统操作".format(yonghu=session.get('username'))
                    log_record(do_thing)
                    return render_template('index.html')
                else:
                    flash('用户名或密码不正确')
                    return render_template('log.html')
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                traceback.print_exc()
                db.rollback()
                # 关闭数据库连接
            db.close()
            return render_template('log.html')
        else:
            flash('验证码错误，请重新输入！')
            return render_template('log.html')
    return render_template('log.html')

@app.route('/system/user_manger/user_show')
def user_show():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    print(u)
    return render_template('user_show.html',u=u)

@app.route('/remove-user/<string:username>/<string:guanli>',methods=['GET','POST'])
def remove_user(username,guanli):
    if guanli=='超级管理员':
        do_thing = "用户：{yonghu}，删除用户操作被拒绝".format(yonghu=session.get('username'))
        log_record(do_thing)
        flash("小样！你不能删除我")
    else:
        db = pymysql.connect("localhost", "root", "123456", "opcdata")
        cursor = db.cursor()
        sql = "Delete FROM user where username="+repr(username)
        print(sql)
        cursor.execute(sql)
        db.commit()
        do_thing = "用户：{yonghu}，删除用户操作执行成功".format(yonghu=session.get('username'))
        log_record(do_thing)
        db.close()
    return redirect('/system/user_manger/user_show')

@app.route('/system/pwd')
def pwd():
    username = session.get('username')
    print('用户名' + username)
    return render_template('changepwd.html', u=username)

@app.route('/system/changepwd',methods=['GET','POST'])
def changepwd():
    #获取当前用户名
    username = session.get('username')
    #根据当前用户名在数据可获取对应密码
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT password FROM user where username="+repr(username)
    cursor.execute(sql)
    realpwd = cursor.fetchall()[0][0]
    print(realpwd)
    print('语句'+sql)
    #获取用户提交的密码
    oldpwd = request.args.get('oldpwd')
    print(oldpwd)
    if oldpwd==realpwd:
        #更新数据库
        if request.args.get('newpwd1') == request.args.get('newpwd2'):
            sql = "update user set password="+repr(request.args.get('newpwd1'))+" where username="+repr(username)
            print('更新'+sql)
            try:
                cursor.execute(sql)
                db.commit()
                do_thing = "用户：{yonghu}，进行了修改密码操作".format(yonghu=session.get('username'))
                log_record(do_thing=do_thing)
                return redirect('/system/user_manger/user_show')
            except:
                traceback.print_exc()
                db.rollback()
        else:
            flash('两次密码输入不一致')
            return redirect('/system/pwd')
    else:
        flash('原密码输入错误')
        return redirect('/system/pwd')
    db.close()

@app.route('/system/logout')
def logout():
    do_thing = "用户：{yonghu}，退出系统".format(yonghu=session.get('username'))
    log_record(do_thing)
    if len(session)!=1:
        print('============================================================')
        session.pop('username')
        return redirect('/')
    else:
        return redirect('/')

@app.route('/system/system_log')
def system_log():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "SELECT * FROM log_info"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    print(u)
    return render_template('system_log.html',u=u)

#日志记录函数
def log_record(do_thing):
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "insert into log_info values (0,{username},{do_what},{do_time},{do_ip})". \
        format(username=repr(session.get('username')),
               do_what=repr(do_thing),
               do_time=repr(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))),
               do_ip=repr(socket.gethostbyname(socket.getfqdn(socket.gethostname()))))
    # print("sql...................",sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        traceback.print_exc()
        db.rollback()