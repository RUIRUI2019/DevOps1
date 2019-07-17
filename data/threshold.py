# -*- coding: utf-8 -*
import pymysql
import time
import traceback

def fun(key_limitValue):
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    while True:
        #yi miao lun xun yici
        sql = "select equipment_id,maxis_speed from equip_data where maxis_speed<{min_value} or maxis_speed " \
              ">{max_value}".format(min_value=key_limitValue['maxis_speed'][0],max_value=key_limitValue['maxis_speed'][1])
        # print(sql)

        try:
            cursor.execute(sql)
            maxis = cursor.fetchall()
            #如果查到超过阈值数据
            if len(maxis)!=0:
                id = []#id存放equipment_id
                for i in maxis:
                    id.append(i[0])
                id = tuple(id)
                print("maxis_id:===================",id)
                # 若problem_info存在该项，则更新；不存在，直接insert;如何判断该项是否存在？
                sql = "select * from problem_info where fault_tag='maxis_speed' and equipment_id in {id}".format(id=id)
                cursor.execute(sql)
                res = cursor.fetchall()
                # print("res:============",res)
                if len(res)==0:
                    #problem_info无该数据，进行insert操作,注意：maxis可能有多组数据，逐条插入
                    for i in maxis:
                        sql = "insert into problem_info values({equipment_id},'主轴转速','maxis_speed',{current_value},{limit_value},{fault_time})".format(
                            equipment_id='\'' + str(i[0]) + '\'', current_value=i[1],limit_value='\''+str(key_limitValue['maxis_speed'][0]) + '-' + str(key_limitValue['maxis_speed'][1])+'\'',
                            fault_time='\'' + str(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())) + '\'')
                        )
                        # print("insert_sql0================" + sql)
                        cursor.execute(sql)
                        db.commit()
                else:
                    #problem_info有该数据，进行update操作
                    id_res = []  # id_res存放equipment_id
                    for i in res:
                        id_res.append(i[0])
                    id_res = tuple(id_res)
                    print ("id_res=====================",id_res)
                    for j in maxis:
                        if j[0] in id_res:
                            # j[0] = j[0].split('')
                            #update操作
                            sql = "update problem_info set current_value ={current_value},fault_time={fault_time} where equipment_id={equipment_id}" \
                                  " and fault_tag ='maxis_speed'".format(current_value=j[1],fault_time='\''+str(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))+'\''),equipment_id='\''+str(j[0])+'\'')
                            # print("update_sql================" + sql)
                            cursor.execute(sql)
                            db.commit()
                        else:
                            sql = "insert into problem_info values({equipment_id},'主轴转速','maxis_speed',{current_value},{limit_value},{fault_time})".format(
                                equipment_id='\''+str(j[0])+'\'', current_value=j[1],limit_value='\''+str(key_limitValue['maxis_speed'][0]) + '-' + str(key_limitValue['maxis_speed'][1])+'\'',
                                fault_time='\''+str(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))+'\'')
                            )
                            # print("insert_sql1================" + sql)
                            cursor.execute(sql)
                            db.commit()
            #无阈值数据
            else:
                continue
        except:
            traceback.print_exc()
            db.rollback()
        try:
            time.sleep(1)
        except IOError:
            break
    db.close()

if __name__ == '__main__':
    key_limitValue={'maxis_speed':[30,96],
                    'current_yield':[300,600],
                    'cycle_time':[200,500],
                    'material_num':[500,800],
                    'speed':[64000,96000],
                    'quanshu':[80,100]}
    fun(key_limitValue)