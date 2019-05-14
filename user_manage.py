from flask import Flask
from flask import render_template,request,flash,session,redirect
import pymysql
import traceback
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route('/',methods=['GET','POST'])
def login():
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
        sql = "update user set password="+repr(request.args.get('newpwd1'))+" where username="+repr(username)
        print('更新'+sql)
        try:
            cursor.execute(sql)
            db.commit()
            return redirect('/system/user_manger/user_show')
        except:
            traceback.print_exc()
            db.rollback()
    else:
        flash('原密码输入错误')
        return redirect('/system/pwd')
    db.close()

@app.route('/system/logout')
def logout():
    if len(session)!=1:
        print('============================================================')
        session.pop('username')
        return redirect('/')
    else:
        return redirect('/')